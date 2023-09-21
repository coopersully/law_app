from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    owner = models.ForeignKey(CustomUser, related_name='events', on_delete=models.CASCADE)