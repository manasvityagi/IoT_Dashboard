from django.contrib import admin
from .models import manufacturer,value_stream,address,Things


# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    search_fields = ('device_type','owner__username',)
    list_display = ('device_type', 'description','owner',)
    list_filter = ('manufacturing_date',)
    fields = ('device_type',)



admin.site.register(Things,CustomAdmin)
