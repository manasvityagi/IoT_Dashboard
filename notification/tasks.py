from time import sleep
from decouple import config
from sendgrid import *

###########################
from celery import Celery, shared_task


#####################
@shared_task
def send_email(email_add):
    sleep(30)
    print('Sending emails, asynchronously, but applications dont suffer, because of celery!')
    sg = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
    user_from_email = Email("manas@thingsboard.com")
    user_to_email = To(email_add)
    user_subject = "Your are registered!"
    user_content = Content("text/plain", "You are on boarded, Now login and enjoy a simpler life!")
    user_mail = Mail(user_from_email, user_to_email, user_subject, user_content)
    response = sg.client.mail.send.post(request_body=user_mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


@shared_task
def send_reset_email(email_add, mail_content):
    sg = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))

    user_from_email = Email("admin@thingsboard.com")
    user_to_email = To(email_add)
    user_subject = "New Password!"
    user_content = Content("text/plain", mail_content)
    user_mail = Mail(user_from_email, user_to_email, user_subject, user_content)
    response = sg.client.mail.send.post(request_body=user_mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
