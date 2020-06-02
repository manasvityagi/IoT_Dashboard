from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from .models import SubscribersList
from .tasks import send_email
from .myform import CustomRegistrationForm, UserUpdateForm, ProfileUpdateForm

from .tasks import sleepy


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
            send_email(registration_form.cleaned_data.get('email'))
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


class GetSubscribersList(ListView):
    template_name = 'users/subscribers_list.html'
    context_object_name = 'subscribers_list_object'

    def get_queryset(self):
        print(SubscribersList.objects.all())
        return SubscribersList.objects.all().order_by('name')
