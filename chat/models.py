from django.db import models
from accounts.models import CustomUser


class Message(models.Model):
    room_name = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
