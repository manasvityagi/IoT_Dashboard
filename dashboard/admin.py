from django.contrib import admin
from django import forms
from .models import Things


# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    extra_field = forms.EmailField()
    search_fields = ('device_type', 'owner__username',)
    list_display = ('device_type', 'description', 'owner', 'extra_field',)
    list_filter = ('manufacturing_date',)
    fields = ('device_type',)


admin.site.register(Things, CustomAdmin)
