from django.core.management.base import BaseCommand, CommandError
from paper.models import Paper
from django.db import connection



class Command(BaseCommand):
    help = 'Uninstall the paper app database tables, with further instructions'

    def drop(self, dbname):
        _DropSQL = "DROP TABLE {}"

        c = connection.cursor()
        try:
            c.execute(_DropSQL.format(dbname))
        finally:
            c.close()
            
    def handle(self, *args, **options):
        #self.drop(Paper._meta.db_table) 
        self.stdout.write(self.style.SUCCESS('Uninstalled the paper app database tables'))
        self.stdout.write('You may need also to:')
        self.stdout.write(' - remove app registration in settings.py')
        self.stdout.write(' - remove use of paper in the forms in other applications')
        self.stdout.write(' - remove use of paper methods in templates or views')
        self.stdout.write('and, optionally:')
        self.stdout.write(' - remove sitewide URLs in url.py')
        self.stdout.write(' - remove the folders and files')
