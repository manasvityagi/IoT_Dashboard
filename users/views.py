import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from .models import SubscribersList
from notification.tasks import send_email, send_reset_email
from .myform import CustomRegistrationForm, UserUpdateForm, ProfileUpdateForm


# function based views
def registration(request):
    if request.method == 'POST':
        print('Its a post')
        registration_form = CustomRegistrationForm(request.POST)
        if registration_form.is_valid():
            print('And its a valid one')
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            email = registration_form.cleaned_data.get('email')
            subscription_choice = registration_form.cleaned_data.get('subscribe')
            if subscription_choice:
                sub = SubscribersList(name=username, email=email)
                sub.save()
            # Add to subscriber's list for important emails
            messages.success(request, f'You are officially registered, {username}!')
            send_email.delay(registration_form.cleaned_data.get('email'))
            return redirect('dashboard-home')
    else:
        registration_form = CustomRegistrationForm()

    context = {
        'title': 'Sign up!',
        'form': registration_form
    }

    return render(request, 'users/registration.html', context)


class OwnerView(CreateView):
    def get(self, request):
        user_update_form = UserUpdateForm()
        profile_update_form = ProfileUpdateForm()

        context = {
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form
        }
        return render(request, 'users/profile.html', context)

    def post(self, request):
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES,
                                                instance=request.user.ownerprofile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Account Updated')
            return redirect('profile')

        messages.success(request, f'Invalid Form')
        return redirect('profile')


class PasswordResetView(CreateView):
    def get(self, request):
        return render(request, 'users/passwordReset.html')

    def post(self, request):
        email = request.POST.get('email_form_field')
        # u = User.objects.get(email__exact=email)[:1].get()
        u = User.objects.filter(email__exact=email).first()
        new_password = random_string()
        u.set_password(new_password)
        u.save()
        send_reset_email(email, new_password)
        messages.success(request, f'Check Email for new password')
        return redirect('login')


class GetSubscribersList(ListView):
    template_name = 'users/subscribers_list.html'
    context_object_name = 'subscribers_list_object'

    def get_queryset(self):
        print(SubscribersList.objects.all())
        return SubscribersList.objects.all().order_by('name')


def random_string(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
