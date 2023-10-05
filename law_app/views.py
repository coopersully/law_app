from django.shortcuts import render

from agenda.models import Event
from announcements.models import Announcement


def home(request):
    if not request.user.is_authenticated:
        context = {'page_name': 'home'}
        return render(request, 'index.html', context)
    else:
        events = Event.objects.all()
        announcements = Announcement.objects.all()
        context = {'page_name': 'home', 'events': events, 'announcements': announcements}
        return render(request, 'dashboard.html', context)