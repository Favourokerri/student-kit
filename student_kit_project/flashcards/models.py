from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

class Card_item(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    question = models.TextField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question
