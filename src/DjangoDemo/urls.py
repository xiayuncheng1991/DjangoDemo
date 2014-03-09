from django.conf.urls import patterns, include, url  
from django.contrib import admin  

from blog.views import *


# Uncomment the next two lines to enable the admin:  
admin.autodiscover()  


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', archive),
)
