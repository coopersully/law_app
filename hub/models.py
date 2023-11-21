from django.db import models
from accounts.models import Program


class UploadedDocument(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
