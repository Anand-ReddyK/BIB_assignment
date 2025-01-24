from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='chat_rooms')

    def __str__(self):
        return self.name