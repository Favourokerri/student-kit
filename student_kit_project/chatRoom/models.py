from django.db import models
from django.contrib.auth.models import User
from user_profile.models import Profile
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    host_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def members(self):
        """ retrive members of room"""
        return Room_Members.objects.filter(room=self)

    def __str__(self):
        return self.name

class Room_Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username