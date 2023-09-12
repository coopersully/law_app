from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from accounts.models import CustomUser


def directory(request):
    role_filter = request.GET.get('role', 'all')
    search_query = request.GET.get('search', '')

    if role_filter.lower() == 'all':
        users = CustomUser.objects.all()
    else:
        users = CustomUser.objects.filter(role=role_filter)

    if search_query:
        users = users.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(username__icontains=search_query)
        )

    users = users.order_by("first_name")

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
