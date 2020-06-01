from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import OwnerProfile


# Purpose of this file is to automatically creat a profile as soon as a user is created
# since, we do not want our user who has registered, to fill in additional form, just
# create a profile, its creation is triggered, and automated

# This gets triggered as soon as the User mode is done with saving the Owner Profile
# post_save is the signal, ideally this file should be called signal handler
@receiver(post_save, sender=User)
def create_owner_profile(sender, instance, created, **kwargs):
    if created:
        OwnerProfile.objects.create(user=instance)


# @receiver(post_save, sender=OwnerProfile)
# def save_owner_profile(sender, instance, **kwargs):
#     instance.save()
