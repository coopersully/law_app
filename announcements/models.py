from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

