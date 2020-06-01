from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import OwnerProfile
from users.models import SubscribersList


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    subscribe = forms.BooleanField()
    house_id = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'subscribe']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = OwnerProfile
        fields = ['image']



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = SubscribersList
        fields = ['name', 'email']
