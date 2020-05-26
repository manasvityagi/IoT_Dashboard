from __future__ import absolute_import, unicode_literals

import os


from celery import Celery

# set the default Django settings module for the 'celery' program.
from decouple import config
from sendgrid import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def send_email(email_add):
    sg = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
    #sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("manas@thingsboard.com")
    to_email = To(email_add)
    subject = "Your are registered!"
    content = Content("text/plain", "You are onboarded, Now login and enjoy a simpler life!")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))