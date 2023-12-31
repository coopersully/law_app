from django.db import models
from accounts.models import Program


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

