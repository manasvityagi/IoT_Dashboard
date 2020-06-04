from django.contrib import admin
from django import forms

from .models import *

# Customizing the admin panel
admin.site.site_header = "THINGSBOARD ADMIN PANEL"


# Demo of Customizing the admin page
class CustomAdminThing(admin.ModelAdmin):
    # Sets the columns that could be displayed in admin site
    list_display = ('device_model_info', 'description', 'purchase_date',)
    search_fields = ('device_model_info',)
    extra_field = forms.EmailField()
    list_filter = ('installed_home_id', 'purchase_date',)
    fields = ('device_model_info',)

    # So when we want to combine a form, when the models are related
    # by foreign keys, we use inline form, which makes sense, because we
    # would have to fill out two forms, for essentially the same logical dataset


#  list_display, search_fields, fields, list_filter, custom_fields and

#  inlines or custom forms


# Inline Forms , when you add a service provider,
# you can add a bunch of service it has provided in the past
class ServiceProviderInline(admin.TabularInline):
    model = ServiceDetails


class ServiceDetailsAdmin(admin.ModelAdmin):
    inlines = [ServiceProviderInline]

    class Meta:
        model = ServiceProvider


admin.site.register(Thing, CustomAdminThing)
admin.site.register(Manufacturer)
admin.site.register(Address)
admin.site.register(Home)
admin.site.register(DeviceModels)
admin.site.register(ValueStream)
admin.site.register(ServiceProvider, ServiceDetailsAdmin)
admin.site.register(Seller)
admin.site.register(ServiceDetails)
admin.site.register(SubscribersList)
