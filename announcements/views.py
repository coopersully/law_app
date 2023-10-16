from django.db.models import Q
from django.shortcuts import render, redirect

from announcements.forms import AnnouncementForm
from announcements.models import Announcement


def announcements(request):
    search_term = request.GET.get('search', '')
    announcements = Announcement.objects.filter(
        Q(title__icontains=search_term) |
        Q(content__icontains=search_term)
    ).order_by('-time_created')
    context = {'page_name': 'announcements', 'announcements': announcements, 'search_term': search_term}
    return render(request, 'announcements/index.html', context)


def announcements_new(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    context = {'page_name': 'announcements', 'form': form}
    return render(request, 'announcements/new.html', context)


def announcement(request, announcement_id):
    bit = Announcement.objects.get(id=announcement_id)
    context = {
        'page_name': 'announcements',
        'announcement': bit
    }

    return render(request, 'announcements/view.html', context)
