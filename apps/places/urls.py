from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object
from places.views import *
from places.models import *
from places.forms import *
from geo.models import City

place_list = {
    "queryset" : Place.objects.all(),
}

city_list_dict = {
    "queryset" : City.objects.all(),
}

urlpatterns = patterns('',
    url(r'^ciudades/?$', object_list, city_list_dict, name='city_list'),
    url(r'^agregar/?$', create_object, place_edit, name='place_add'),
    url(r'^(?P<city_slug>[-\w]+)/?$', city_list, name='place_city_list'),
    url(r'^(?P<city_slug>[-\w]+)/agregar/?$', place_city_add, name='place_city_add'),
    url(r'^(?P<city_slug>[-\w]+)/buscar/?$', place_search, name='place_search'),
    url(r'^(?P<city_slug>[-\w]+)/(?P<slug>[-\w]+)/?$', city_list, name='place_city_category'),
    url(r'^(?P<city_slug>[-\w]+)/(?P<place_slug>[-\w]+)/?$', place_detail, name='place_detail'),
    url(r'^(?P<city_slug>[-\w]+)/(?P<place_slug>[-\w]+)/editar/?$', place_edit, name='place_edit'),
    #url(r'^(?P<city_slug>[-\w]+)/(?P<place_slug>[-\w]+)/editar/?$', update_object, dict(place_edit,slug_field='slug'), name='place_edit2'),
    #url(r'^/agregar$',agregar_parahacer, name='agregar_parahacer'),
)
