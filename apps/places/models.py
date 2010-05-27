from django.utils.translation import ugettext_lazy as _
from django.db import models
from geo.models import City
from django.template.defaultfilters import slugify
from django.db.models import Q
import re

class Category(models.Model):
    name = models.CharField(_('Nombre'),max_length=50)
    slug = models.SlugField(_('Slug'),max_length=50)
    desc = models.CharField(_('Descripcion'),max_length=250,null=True,blank=True)

    def __unicode__(self):
        return self.name
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.name)
        super(Category,self).save(force_insert,force_update)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categorias'


class Place(models.Model):
    name = models.CharField(_('Nombre'),max_length=50)
    slug = models.SlugField(_('Slug'),max_length=50)
    desc = models.CharField(_('Descripcion'),max_length=250,null=True,blank=True)
    city = models.ForeignKey(City,verbose_name=_('Ciudad'))
    category = models.ForeignKey(Category,verbose_name=_('Categoria'))
    address = models.CharField(_('Direccion'),max_length=50,null=True,blank=True)
    tel = models.CharField(_('Telefono'),max_length=20,null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    
    #user = models.ForeignKey(User,verbose_name=_('Usuario'))
    created = models.DateTimeField(_('created datetime'),auto_now_add=True)

    active = models.BooleanField(default=True)

    lat = models.FloatField(_('Lat'),null=True,blank=True)
    lon = models.FloatField(_('Long'),null=True,blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'sitios'
        unique_together = (('name','city'),('slug','city'))
    def __unicode__(self):
        return self.name
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.name)
        super(Place,self).save(force_insert,force_update)

    @property
    def country(self):
        return self.city.country
    @models.permalink
    def get_absolute_url(self):
        return ('place_detail',[self.city.slug,self.slug])

def add_place(name,city,address=None,tel=None,active=True):
    if isinstance(city,str) or isinstance(city,unicode):
        city = City.objects.get(Q(name=ciudad)|Q(abrev=city))
    obj = Sitio(name=name,city=city,dir=dir,active=active)
    obj.save()

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

