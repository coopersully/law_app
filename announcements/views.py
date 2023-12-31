from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from announcements.forms import AnnouncementForm
from announcements.models import Announcement


@login_required
def announcements(request):
    search_term = request.GET.get('search', '')
    announcements = Announcement.objects.filter(
        Q(title__icontains=search_term) |
        Q(content__icontains=search_term)
    ).order_by('-time_created')

    if (request.user.role != 'admin' and request.user.role != 'admin'):
        announcements = announcements.filter(program=request.user.program)

    # check if allowed user
    allowedRoles = ['staff', 'Staff', 'admin', 'Admin']
    allowed_user = any([request.user.role == allowedRole for allowedRole in allowedRoles])

    context = {'page_name': 'announcements', 'announcements': announcements, 'search_term': search_term,
               'allowed_user': allowed_user}
    return render(request, 'announcements/index.html', context)


@login_required
def announcements_new(request):
    # Check if the user is an admin (staff or superuser)
    allowedRoles = ['staff', 'Staff', 'admin', 'Admin']
    if not (any([request.user.role == allowedRole for allowedRole in allowedRoles])):
        return HttpResponseForbidden("You don't have permission to access this page.")

    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm()

    context = {'page_name': 'announcements', 'form': form}
    return render(request, 'announcements/new.html', context)


@login_required
def announcement(request, announcement_id):
    bit = Announcement.objects.get(id=announcement_id)
    context = {
        'page_name': 'announcements',
        'announcement': bit
    }

    return render(request, 'announcements/view.html', context)
