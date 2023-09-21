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
    return render(request, 'announcements/index.html', {'announcements': announcements, 'search_term': search_term})


def announcements_new(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/new.html', {'form': form})
