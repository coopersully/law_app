from django.shortcuts import render
from django.views import generic

from accounts.models import CustomUser


def directory(request):
    # Gets the 'role' query parameter, defaults to 'all'
    role_filter = request.GET.get('role', 'all')

    if role_filter.lower() == 'all':
        users = CustomUser.objects.order_by("first_name")
    else:
        users = CustomUser.objects.filter(role=role_filter).order_by("first_name")

    context = {
        'page_name': 'directory',
        'users': users,
        'current_role_filter': role_filter
    }

    return render(request, 'directory.html', context)


def profile(request, username: str):
    person = CustomUser.objects.get(username=username)
    context = {
        'page_name': 'directory',
        'person': person
    }
    return render(request, 'user.html', context)
