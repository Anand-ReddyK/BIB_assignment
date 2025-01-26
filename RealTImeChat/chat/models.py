from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Messages(models.Model):
    conversation = models.ForeignKey(ChatRoom, related_name="conversation", on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("created_at",)