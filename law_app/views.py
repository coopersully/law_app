from django.shortcuts import render

from law_app import settings

import requests, json

from agenda.models import Event
from announcements.models import Announcement

def getWeather(location):
    api_key = settings.OPEN_WEATHER
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = location
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    return {
        'tempF': (x['main']['temp']-273.15)*(9/5)+32,
        'tempC': x['main']['temp']-273.15,
        'clouds': x['clouds']['all']
    }

def home(request):
    if not request.user.is_authenticated:
        context = {'page_name': 'home'}
        return render(request, 'index.html', context)
    else:
        weather = getWeather(request.user.program.location)
        events = Event.objects.all()
        announcements = Announcement.objects.all()
        context = {'page_name': 'home', 'events': events, 'announcements': announcements, 'tempF': weather['tempF'], 'tempC': weather['tempC'], 'clouds': weather['clouds']}
        return render(request, 'dashboard.html', context)