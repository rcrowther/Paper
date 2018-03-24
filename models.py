from django.db import models
import datetime
from django.urls import reverse



class PaperManager(models.Manager):
  
    def create(self, obj):
        '''
        Create.
        @return the created object.
        '''
        obj.save()
        return obj  
          
    def update(self, obj):
        '''
        Update.
        @return the updated object.
        '''
        obj.mod_date=datetime.datetime.now()
        obj.save()
        return obj
  
    def delete(self, obj):
        '''
        Delete.
        @return the deleted object.
        '''
        obj.delete()
        return obj
        

class Paper(models.Model):
    title = models.CharField(
      max_length=64,
      db_index=True,
      unique=True,
      help_text="Name for the article. Max 64 characters.",
      )
      
    slug = models.SlugField(
      db_index=True,
      unique=True,
      help_text="Short name for use in urls.",
      )
      
    summary = models.CharField(
      max_length=400,
      help_text="Teaser for explaination of the content. Max 400 characters.",
      )
      
    # uneditable, visible
    create_date = models.DateTimeField('date created.', auto_now_add=True)
    
    # uneditable, visible
    mod_date = models.DateTimeField('date last modified.', auto_now_add=True)
    
    # uneditable, visible
    pub_date = models.DateTimeField('date published.',
     auto_now_add=True
    )
    
    #! length not enforced internally. Add validation?
    body = models.TextField(
      blank=True,
      default='',
      max_length=8000,
      help_text="Main text of article. Max 8000 characters.",
      )
      
    author = models.CharField(
      max_length=64,
      blank=True, 
      default='',
      help_text="Name of the author.",
      )

    objects = models.Manager()
    system = PaperManager()
    
    def get_absolute_url(self):
        return reverse('paper-detail', args=[str(self.id)])
    
    def __str__(self):
        return "{0}".format(self.title)
  
