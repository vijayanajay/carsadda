from django.conf.urls import patterns, url

from getcarsdata import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)