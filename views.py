from django.shortcuts import render

from django import forms
from quickviews import ModelCreateView, ModelUpdateView, ModelDeleteView, ModelListView, ModelDetailView
from quickviews import inline_templates

from .models import Paper



class PaperListView(ModelListView):
    model=Paper
    use_fields=['title', 'create_date', 'mod_date']
    rows_per_page=25



class PaperDetailView(ModelDetailView):
    model = Paper
    url_pk_arg = 'paper_pk'    
    use_fields = ['title', 'summary', 'pub_date']
    object_name_field_key = 'title'



from django.forms import ModelForm

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'slug', 'summary', 'body', 'author']


  
class PaperCreateView(ModelCreateView):
    model = Paper
    object_name_field_key = 'title'
    #fields = ['title', 'slug', 'summary', 'body', 'author']
    form_class = PaperForm
    success_url = '/paper/'
        
    def success_action(self, form):
        obj = Paper.system.create(form.instance)
        return obj


    
class PaperUpdateView(ModelUpdateView):
    model = Paper
    url_pk_arg = 'paper_pk'
    object_name_field_key = 'title'
    #fields = ['title', 'slug', 'summary', 'body', 'author']
    form_class = PaperForm
    success_url = '/paper/'

    def success_action(self, form):
        obj = Paper.system.update(form.instance)
        return obj



class PaperDeleteView(ModelDeleteView):
    model = Paper
    url_pk_arg = 'paper_pk'
    object_name_field_key = 'title'
    success_url = '/paper/'

