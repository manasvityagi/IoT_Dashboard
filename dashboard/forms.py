from django import forms

from dashboard.models import Things


class add_device_form(forms.ModelForm):
    description = forms.CharField(label='Description', max_length=100)
    device_type = forms.CharField(label='Device Type', max_length=100)

    class Meta:
        model = Things
        fields = ('description','device_type',)