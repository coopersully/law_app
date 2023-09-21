from django.shortcuts import render, redirect

from agenda.forms import EventForm
from agenda.models import Event


def agenda(request):
    all_events = Event.objects.all()
    return render(request, 'agenda/index.html', {'events': all_events})


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

    return render(request, 'agenda/new.html', {'form': form})
