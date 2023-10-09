from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200, default='Cambridge')
    map = models.URLField(max_length=500, default='https://maps.app.goo.gl/J5oJ5SHma4qW7UHs5')
    datetime = models.DateTimeField()
    owner = models.ForeignKey(CustomUser, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

