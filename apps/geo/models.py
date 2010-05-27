from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class Country(models.Model):
    name = models.CharField(_('Nombre'),max_length=50)
    abrev = models.CharField(_('Abreviacion'),max_length=6,null=True,blank=True)
    slug = models.SlugField(_('Slug'),max_length=50,null=True,blank=True)
    
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['name']
        unique_together = (('name',),)

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.name)
        super(Country,self).save(force_insert,force_update)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(_('Nombre'),max_length=50)
    abrev = models.CharField(_('Abreviacion'),max_length=6,null=True,blank=True)
    slug = models.SlugField(_('Slug'),max_length=50,null=True,blank=True)
    country = models.ForeignKey(Country,verbose_name=_('Pais'))
    lon = models.FloatField(_('Long'),null=True,blank=True)
    lat = models.FloatField(_('Lat'),null=True,blank=True)
    
    class Meta:
        verbose_name_plural = 'Ciudades'
        unique_together = (('name','country'),)
        ordering = ['name']

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.name)
        super(City,self).save(force_insert,force_update)

    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('place_city_list',[self.slug])
