from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "phone_number", "school_email", "student_id")
        labels = {
            'school_email': 'Samford Email address',
            'student_id': 'Samford Student ID'
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "bio", "email", "phone_number", "school_email", "student_id")
        labels = {
            'school_email': 'Samford Email address',
            'student_id': 'Samford Student ID',
            'bio': 'Biography'
        }