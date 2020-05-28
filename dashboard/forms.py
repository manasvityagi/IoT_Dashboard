from django import forms

from django.contrib.auth.models import User

from dashboard.models import Thing


class add_device_form(forms.ModelForm):
    # description = forms.CharField(label='Description', max_length=100)
    # device_type = forms.CharField(label='Device Type', max_length=100)
    #

    class Meta:
        model = Thing
        fields = ('device_model_info', 'description'
                  , 'installed_home_id', 'purchase_date','life_used')