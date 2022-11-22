from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    message_1 = models.TextField(null=True, blank=True)
    message_2 = models.TextField(null=True, blank=True)
    message_3 = models.TextField(null=True, blank=True)
    message_4 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"