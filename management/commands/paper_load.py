import csv
import traceback
import collections
import os
from django.conf import settings


from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.core.management import call_command
from paper.models import Paper
#from testtable.tabledata import tabledata, to_string, exists

PaperFieldNames = ['title','slug','summary','create_date','mod_date','pub_date','body','author',]

TableData = collections.namedtuple('TableData', 'description count filepath')

tabledata = {
'DutchPainters' : TableData("Dutch Painters and brief details.", 12, 'csv/dutch_painters.csv'
),
}


def extendto(size, b):
    l = 0
    for s in b:
      l += len(s)
    if l < size:
      b.append(' ' *(size - l))
      
def to_string():
    b = []
    b.append('Available tables:')
    for k,v in tabledata.items():
        bb = []
        bb.append("  ")
        bb.append(k)
        extendto(16, bb)
        bb.append("size:")
        bb.append(str(v.count))
        extendto(28, bb)
        bb.append(v.description)
        b.append('\n')
        b.extend(bb)  
    return ''.join(b)
        

class Command(BaseCommand):
    help = 'Add data to the Paper database table'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('table', nargs='?', default='', type=str)

    def mkdb(self, data):
        success = False
        fp = os.path.join(settings.BASE_DIR, 'paper', data.filepath)
        with open(fp, 'r') as f:
            reader = csv.reader(f)
            # if a big CSV file creaks, stash useful vars
            idx = -1
            zrow = ()
            try:
                for idx, row in enumerate(reader):
                    # split row into dict
                    zrow = zip(PaperFieldNames, row)
                    d = dict(zrow)
                    o = Paper(**d)
                    #if (verbose):
                    #self.stdout.write('.', ending='')
                    #self.stdout.write(str(d))
                    o.save()
                success = True
            except Exception as err:
                self.stdout.write('line no:' + str(idx))
                self.stdout.write(str(d))
                #! fix
                #! write error message
                #err.__traceback__.print_tb()
                traceback.print_tb(err.__traceback__, limit=1)
        return (success, idx)

    def print_dbs(self):
        self.stdout.write(to_string())
        
    def handle(self, *args, **options):
        call_command("migrate", '--run-syncdb')

        if (not options['table']):
            self.print_dbs()
            return

        #self.verbosity
        table = options['table']
        try:
          table_data = tabledata[table]
        except KeyError:
            self.stdout.write('db data "{0}" not available (try run "load" with no commands)'.format(
            table
            ))
            return
        count = Paper.objects.count()
        if(count > 0):
            self.stdout.write('db table must be empty, but is populated with {1} data items?'.format(
            table,
            count
            ))
            return
        self.stdout.write('Loading the db table with data. This may take some time...')
        success, idx = self.mkdb(table_data)
        if(success):
            self.stdout.write('db table is populated')
        else:
            self.stdout.write('db table failed to populate? Some data may have been written')
        self.stdout.write('{} entries written'.format(idx + 1))
        self.stdout.write('Done')
       
