from django.contrib import admin
from django import forms
from .models import *


# Demo of
class CustomAdmin(admin.ModelAdmin):
    extra_field = forms.EmailField()
    search_fields = ('device_model_info',)
    list_display = ('device_model_info', 'description',)
    list_filter = ('installed_home_id',)
    fields = ('device_model_info',)


admin.site.register(Thing, CustomAdmin)
admin.site.register(Manufacturer)
admin.site.register(Address)
admin.site.register(Home)
admin.site.register(DeviceModels)
admin.site.register(ValueStream)
admin.site.register(ServiceProvider)
admin.site.register(Seller)
