from django.conf.urls import url

from .models import Paper
from . import views


urlpatterns = [
    url(r'^add/$', views.PaperCreateView.as_view(), name='add'),
    url(r'^(?P<paper_pk>[0-9]+)/edit/$', views.PaperUpdateView.as_view(), name='edit'),
    url(r'^(?P<paper_pk>[0-9]+)/delete/$', views.PaperDeleteView.as_view(), name='delete'),
    url(r'^(?P<paper_pk>[0-9]+)/$', views.PaperDetailView.as_view(), name='detail'),
    url(r'^$', views.PaperListView.as_view(), name='index'),
]
