from django.conf.urls import include, url

from . import views


url_list = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]

urlpatterns = [
    url(r'', include(url_list, namespace='palestra')),
]
