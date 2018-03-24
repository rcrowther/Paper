from django.conf.urls import url

from .models import Paper
from . import views

try:
    import quickviews
    from . import quickviews
    qv_urlpatterns = [
    url(r'^qv/add/$', quickviews.PaperCreateView.as_view(), name='qv-paper-add'),
    url(r'^qv/(?P<paper_pk>[0-9]+)/edit/$', quickviews.PaperUpdateView.as_view(), name='qv-paper-edit'),
    url(r'^qv/(?P<paper_pk>[0-9]+)/delete/$', quickviews.PaperDeleteView.as_view(), name='qv-paper-delete'),
    url(r'^qv/(?P<paper_pk>[0-9]+)/$', quickviews.PaperDetailView.as_view(), name='qv-paper-detail'),
    url(r'^qv$', quickviews.PaperListView.as_view(), name='qv-paper-list'),
    ]
except ImportError:
    qv_urlpatterns = []
    
urlpatterns = [
    url(r'^add/$', views.PaperCreate.as_view(), name='paper-add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.PaperUpdate.as_view(), name='paper-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PaperDelete.as_view(), name='paper-delete'),
    url(r'^(?P<pk>[0-9]+)/$', views.PaperDetail.as_view(), name='paper-detail'),
    url(r'^$', views.PaperList.as_view(), name='paper-list'),
] + qv_urlpatterns
  
