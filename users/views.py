from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages  # for flash messages
from django.views import View
from django.views.generic import CreateView

from .tasks import send_email
from .myform import CustomRegistrationForm


def registration(request):
    if request.method == 'POST':
        print('Its a post')
        registration_form = CustomRegistrationForm(request.POST)
        if registration_form.is_valid():
            print('And its a valid one')
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'You are officially registered, {username}!')
            # async task via celery
            send_email(registration_form.cleaned_data.get('email'))
            return redirect('dashboard-home')
    else:
        registration_form = CustomRegistrationForm()

    context = {
        'title': 'Sign up',
        'form': registration_form
    }

    return render(request, 'users/registration.html', context)


@login_required
def owner_profile(request):
    return render(request, 'users/profile.html')


class OwnerView(CreateView):
    def get(self, request):
        return render(request, 'users/profile.html')
