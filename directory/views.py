from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

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

    if request.user.role != 'admin':
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


@login_required
def change_user_role(request, user_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to change roles.')
        return redirect(profile, username=request.user.username)

    if request.method == 'POST':
        new_role = request.POST.get('role')
        user_to_change = CustomUser.objects.get(id=user_id)

        if user_to_change:
            user_to_change.role = new_role
            user_to_change.save()
            messages.success(request, 'User role changed successfully.')
            return redirect(profile, username=user_to_change.username)
        else:
            messages.error(request, 'User not found.')

    return redirect(directory)
