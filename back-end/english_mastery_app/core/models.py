from django.db import models
from django.utils import timezone

class WordOfTheDay(models.Model):
    word = models.CharField(max_length=200)
    definition = models.TextField()
    date = models.DateField(default=timezone.now)

class ChatMessage(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
