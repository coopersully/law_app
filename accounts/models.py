from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
        ('admin', 'Administrator'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    school_email = models.EmailField(max_length=254, unique=True)
    student_id = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Add related_name to prevent reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',  # Add a unique related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Add a unique related_name
        related_query_name='user',
    )

    def __str__(self):
        return self.username
