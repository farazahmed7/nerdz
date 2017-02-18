from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class UserEvent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
