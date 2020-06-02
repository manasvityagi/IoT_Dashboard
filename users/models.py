from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class OwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='owner_pics/default.jpg', upload_to='owner_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class SubscribersList(models.Model):
    name = models.CharField(max_length=150, default='Joe')
    email = models.EmailField()

    def __str__(self):
        return str(self.name + " " + self.email)
