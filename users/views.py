from django.shortcuts import render, redirect
from django.contrib import messages # for flash messages
from .myform import CustomRegistrationForm


# Create your views here.
def registration(request):

    if(request.method == 'POST'):
        print('Its a post')
        registration_form = CustomRegistrationForm(request.POST)
        if registration_form.is_valid():
            print('And its a valid one')
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, 'Congratulations! User Registered')
            return redirect('dashboard-info')
    else:
        registration_form = CustomRegistrationForm()


    context = {
        'title': 'Sign up',
        'form': registration_form
    }

    return render(request,'users/registration.html', context)
