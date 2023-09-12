from django.shortcuts import render
from django.views import generic

from accounts.models import CustomUser


def directory(request):
    # show all users
    # show only professors
    # show only students?
    users = CustomUser.objects.order_by("first_name")
    context = {
        'page_name': 'directory',
        'users': users
    }
    return render(request, 'directory.html', context)


def profile(request, username: str):
    person = CustomUser.objects.get(username=username)
    context = {
        'page_name': 'directory',
        'person': person
    }
    return render(request, 'user.html', context)
