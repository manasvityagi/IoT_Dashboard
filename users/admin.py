from django.contrib import admin

# Register your models here.
from users.models import OwnerProfile, SubscribersList

admin.site.register(OwnerProfile)
admin.site.register(SubscribersList)