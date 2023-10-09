from django import forms
from django.forms import DateTimeInput, TextInput

from agenda.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'map', 'datetime']
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
            'location': TextInput(attrs={'id': 'locationInput'}),
            'map': TextInput(attrs={'id': 'mapInput'}),
        }