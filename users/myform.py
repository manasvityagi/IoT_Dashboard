from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    house_id = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','house_id', 'email','password1','password2']