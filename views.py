from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paper



class PaperDetail(DetailView):
    model = Paper
    #template_name="paper/page.html"
   
   
   
class PaperList(ListView):
    model = Paper


class PaperCreate(CreateView):
    model = Paper
    fields = ['title', 'slug', 'summary', 'body', 'author']

class PaperUpdate(UpdateView):
    model = Paper
    fields = ['title', 'slug', 'summary', 'body', 'author']

class PaperDelete(DeleteView):
    model = Paper
    success_url = reverse_lazy('paper-list')
