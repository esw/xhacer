from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/?(.*)',admin.site.root),
    url(r'^login$', 'django.contrib.auth.views.login', name="acct_login"),
    url(r'^logout$', 'django.contrib.auth.views.logout', name="acct_logout"),
    url(r'^$', 'django.views.generic.simple.redirect_to',{'url':'/barranquilla', 'permanent': False}, name='index'),
    url(r'^', include('places.urls')),
    # PRUEBA EDICION JOSE!!!
)
