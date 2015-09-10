from django.conf.urls import include, url

from . import views


url_list = [
    url(r'^palestra/$', views.PalestraListView.as_view(), name='palestra_list'),
    url(r'^palestra/(?P<slug>[\w-]+)/$', views.PalestraDetailView.as_view(), name='palestra'),
    url(r'^tag/$', views.TipoTagListView.as_view(), name='tipotag_list'),
]

urlpatterns = [
    url(r'', include(url_list, namespace='palestra')),
]
