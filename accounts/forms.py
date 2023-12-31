from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username", "first_name", "last_name", "email", "phone_number", "school_email", "student_id", "program")
        labels = {
            'email': 'Personal Email address',
            'school_email': 'School Email address',
            'student_id': 'School Student ID'
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("profile_pic", "username", "first_name", "last_name", "bio", "email", "phone_number", "school_email",
                  "student_id")
        labels = {
            'profile_pic': 'Profile Picture',
            'email': 'Personal Email address',
            'school_email': 'School Email address',
            'student_id': 'School Student ID',
            'bio': 'Biography'
        }
