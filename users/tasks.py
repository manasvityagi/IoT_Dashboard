# from __future__ import absolute_import, unicode_literals
# import os
#
# from celery import shared_task
from time import sleep

# set the default Django settings module for the 'celery' program.
from decouple import config
from sendgrid import *

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IoT_Dashboard.settings')


#
# app = Celery('proj')
#
# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

###########################
from celery import Celery, shared_task

app = Celery('tasks', broker='amqp://localhost')


@app.task
def add(x, y):
    return x + y


#####################
@shared_task
def send_email(email_add):
    sg = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))

    user_from_email = Email("manas@thingsboard.com")
    user_to_email = To(email_add)
    user_subject = "Your are registered!"
    user_content = Content("text/plain", "You are onboarded, Now login and enjoy a simpler life!")
    user_mail = Mail(user_from_email, user_to_email, user_subject, user_content)
    response = sg.client.mail.send.post(request_body=user_mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
