from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from accounts.models import CustomUser


@login_required
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

    if (request.user.role != 'admin' and request.user.role != 'admin'):
        users = users.filter(program=request.user.program)

    users = users.order_by("first_name")

    context = {
        'page_name': 'directory',
        'users': users,
        'current_role_filter': role_filter
    }

    return render(request, 'directory.html', context)


@login_required
def profile(request, username: str):
    person = CustomUser.objects.get(username=username)
    context = {
        'page_name': 'directory',
        'person': person
    }
    return render(request, 'user.html', context)
