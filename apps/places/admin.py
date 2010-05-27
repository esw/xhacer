from django.contrib import admin
from places.models import Place, Category

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','desc','city','address','tel','url','active','lon','lat')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']
    list_filter = ('city',)

admin.site.register(Place,PlaceAdmin)
admin.site.register(Category)
