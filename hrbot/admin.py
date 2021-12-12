from django.contrib import admin

from . import models
# Register your models here.

class HRWork(admin.ModelAdmin):
    list_display = ['name','town','time_update', 'time_create']
    search_fields = ['name','town']
    #list_editable = ['ame', 'description']
class HRCity(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(models.Work, HRWork)
admin.site.register(models.City, HRCity)