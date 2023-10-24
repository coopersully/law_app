from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from agenda.forms import EventForm
from agenda.models import Event


@login_required
def agenda(request):
    search_query = request.GET.get('search', '')
    sort_filter = request.GET.get('sort', 'date')

    # Fetch all events
    events = Event.objects.all()
    if (request.user.role != 'admin' and request.user.role != 'admin'):
        events = events.filter(program=request.user.program)

    # Apply the search filter
    if search_query:
        events = events.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)  # Assuming that 'description' is a field on your Event model
        )

    # Apply the sort filter
    if sort_filter == 'date':
        events = events.order_by('datetime')
    elif sort_filter == 'title':
        events = events.order_by('title')

    # check if allowed user
    allowedRoles = ['staff', 'Staff', 'admin', 'Admin']
    allowed_user = any([request.user.role == allowedRole for allowedRole in allowedRoles])

    context = {
        'page_name': 'agenda',
        'events': events,
        'current_sort_filter': sort_filter,
        'allowed_user': allowed_user
    }

    return render(request, 'agenda/index.html', context)


@login_required
def event(request, event_id):
    bit = Event.objects.get(id=event_id)

    context = {
        'page_name': 'events',
        'event': bit
    }

    return render(request, 'agenda/view.html', context)


@login_required
def agenda_new(request):
    # Check if the user is an admin (staff or superuser)
    allowedRoles = ['staff', 'Staff', 'admin', 'Admin']
    if not (any([request.user.role == allowedRole for allowedRole in allowedRoles])):
        return HttpResponseForbidden("You don't have permission to access this page.")

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
