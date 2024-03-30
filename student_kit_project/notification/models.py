from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Welcome_Notification(models.Model):
    """ notifications ment for new members"""
    title = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class General_Notification(models.Model):
    """ notifications ment for everyone"""
    users_seen = models.ManyToManyField(User, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Notification(models.Model):
    """ personal notifications"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
