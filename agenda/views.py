from django.shortcuts import render, redirect

from agenda.forms import EventForm
from agenda.models import Event


def agenda(request):
    all_events = Event.objects.all()
    context = {'page_name': 'agenda', 'events': all_events}
    return render(request, 'agenda/index.html', context)

def event(request, event_id):
    meeting = Event.objects.get(id=event_id)
    context = {
        'page_name': 'event',
        'event': meeting
    }

    return render(request, 'agenda/event.html', context)

def agenda_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.owner = request.user
            new_event.save()
            return redirect('agenda')
    else:
        form = EventForm()

    context = {'page_name': 'agenda', 'form': form}
    return render(request, 'agenda/new.html', context)
