from django import forms
from django.forms import inlineformset_factory, DateField, Textarea

from django.contrib.auth.models import User

from dashboard.models import *


class add_address(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street', 'zip',)


class add_device(forms.ModelForm):
    # description = forms.CharField(label='Description', max_length=100)
    # device_type = forms.CharField(label='Device Type', max_length=100)
    #

    class Meta:
        model = Thing
        # fields = ('description',)
        fields = ('description', 'device_model_info', 'installed_home_id',
                  'purchase_date', 'life_used',)

        widgets = {
            'purchase_date': forms.DateInput(format='%m/%d/%Y',
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }


class add_address(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street', 'zip',)


class add_manufacturer(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'address', 'phone_number', 'is_certified',)


class add_device_models(forms.ModelForm):
    class Meta:
        model = DeviceModels
        fields = ('name', 'max_life', 'warranty_days', 'image', 'energy_rating',
                  'safety_rating', 'current_consumption', 'mfg',
                  'model_number', 'serial_number',)


class add_home(forms.ModelForm):
    class Meta:
        model = Home
        fields = ('owner', 'address',)


class add_service_provider(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ('name', 'address', 'phone_number', 'type_of_device_handled',)


class add_seller(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('name', 'address', 'phone_number', 'type_of_device_sold',)
