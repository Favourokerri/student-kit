from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static 
import uuid

# Create your models here.

class Profile(models.Model):
    """ user profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    first_time_login = models.BooleanField(default=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(default="i am a good kid")

    def __str__(self):
        return self.email