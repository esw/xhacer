from django.contrib import admin
from geo.models import Country, City

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name','abrev','slug')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name','abrev','slug','country','lat','lon')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('country',)
    search_fields = ['name']

admin.site.register(Country,CountryAdmin)
admin.site.register(City,CityAdmin)
