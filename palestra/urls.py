from django.conf.urls import include, url

from . import views


url_list = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^palestra/$', views.PalestraListView.as_view(), name='palestra_list'),
]

urlpatterns = [
    url(r'', include(url_list, namespace='palestra')),
]
