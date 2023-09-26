from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from agenda.models import Event
from announcements.models import Announcement


def home(request):
    context = {'page_name': 'home'}
    return render(request, 'index.html', context)


@login_required
def dashboard(request):

    events = Event.objects.all()
    announcements = Announcement.objects.all()

    context = {'page_name': 'dashboard', 'events': events, 'announcements': announcements}
    return render(request, 'dashboard.html', context)
