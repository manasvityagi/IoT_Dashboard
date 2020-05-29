from django import forms

from django.contrib.auth.models import User

from dashboard.models import *


class add_device(forms.ModelForm):
    # description = forms.CharField(label='Description', max_length=100)
    # device_type = forms.CharField(label='Device Type', max_length=100)
    #

    class Meta:
        model = Thing
        # fields = ('description',)
        fields = ('description',)


class add_manufacturer(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'address', 'phone_number', 'is_certified',)
        #fields = ('name', 'phone_number', 'is_certified',)

#
# class add_seller(forms.ModelForm):
#
#     class Meta:
#         model = Thing
#         fields = ('description', )
#
#
# class add_service_provider(forms.ModelForm):
#
#     class Meta:
#         model = Thing
#         fields = ('description', )
