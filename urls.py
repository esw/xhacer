from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/(.*)',admin.site.root),
    url(r'^login$', 'django.contrib.auth.views.login', name="acct_login"),
    url(r'^logout$', 'django.contrib.auth.views.logout', name="acct_logout"),
    url(r'^', include('places.urls')),
)
