from datetime import datetime

from django.shortcuts import render

from law_app import settings

import requests, json

from agenda.models import Event
from announcements.models import Announcement


def get_weather(location):
    api_key = settings.OPEN_WEATHER
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = location
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print(x)
    return {
        'tempF': int((x['main']['temp'] - 273.15) * (9 / 5) + 32),
        'tempC': int(x['main']['temp'] - 273.15),
        'clouds': x['clouds']['all'],
        'icon': x['weather'][0]['icon'],
        'name': x['name']
    }


def get_time_of_day():
    current_time = datetime.now().time()
    if current_time.hour < 12:
        return 'morning'
    elif 12 <= current_time.hour < 17:
        return 'afternoon'
    elif 17 <= current_time.hour < 20:
        return 'evening'
    else:
        return 'night'


def home(request):
    if not request.user.is_authenticated:
        context = {'page_name': 'home'}
        return render(request, 'index.html', context)
    else:
        weather = get_weather(request.user.program.location)
        time_of_day = get_time_of_day()
        events = Event.objects.all()
        announcements = Announcement.objects.all()
        context = {
            'page_name': 'home',
            'events': events,
            'announcements': announcements,
            'tempF': weather['tempF'],
            'tempC': weather['tempC'],
            'clouds': weather['clouds'],
            'icon': weather['icon'],
            'name': weather['name'],
            'time_of_day': time_of_day  # Adding time of day here
        }
        return render(request, 'dashboard.html', context)
