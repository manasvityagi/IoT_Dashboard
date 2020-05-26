from django.shortcuts import render, redirect
from django.contrib import messages # for flash messages
from .myform import CustomRegistrationForm
import sendgrid
import os
from sendgrid.helpers.mail import *


# Create your views here.
def send_email(email_add):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("manas@thingsboard.com")
    to_email = To(email_add)
    subject = "Your are registered!"
    content = Content("text/plain", "You are onboarded, Now login and enjoy a simpler life!")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def registration(request):
    print(os.environ.get('SENDGRID_API_KEY'))
    if(request.method == 'POST'):
        print('Its a post')
        registration_form = CustomRegistrationForm(request.POST)
        if registration_form.is_valid():
            print('And its a valid one')
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'You are officially registered, {username}!')
            send_email(registration_form.cleaned_data.get('email'))
            return redirect('dashboard-info')
    else:
        registration_form = CustomRegistrationForm()


    context = {
        'title': 'Sign up',
        'form': registration_form
    }

    return render(request,'users/registration.html', context)


def logout(request):
    logout(request)
