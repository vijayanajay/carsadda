from django.conf.urls import patterns, include, url
from django.contrib import admin
from getcarsdata import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getcarinfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^getcardata/', include('getcarsdata.urls')),
)
