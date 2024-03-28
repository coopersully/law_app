import hashlib
import hmac
import subprocess
from datetime import datetime
from venv import logger

import requests
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from agenda.models import Event
from announcements.models import Announcement
from law_app import settings
from law_app.settings import GITHUB_SECRET_TOKEN


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
        program = request.user.program

        location: str
        if program is None:
            location = "Cambridge, GB"
        else:
            location = program.location

        weather = get_weather(location)
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


@csrf_exempt
@require_POST
def github_webhook(request):
    try:
        # Get the signature sent by GitHub
        github_signature = request.headers.get('X-Hub-Signature-256')
        if not github_signature:
            logger.warning('No GitHub signature provided.')
            return JsonResponse({'error': 'No GitHub signature provided.'}, status=403)

        # Compute the hash using the request body and your secret token
        signature = 'sha256=' + hmac.new(GITHUB_SECRET_TOKEN.encode(), request.body, hashlib.sha256).hexdigest()

        # Verify if the computed hash matches GitHub's hash
        if not hmac.compare_digest(github_signature, signature):
            logger.warning('GitHub signature does not match.')
            return JsonResponse({'error': 'GitHub signature does not match.'}, status=403)

        # If the hash matches, execute the script
        result = subprocess.run(['/var/www/law_app/pull_changes.sh'], capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f'Error executing script: {result.stderr}')
            return JsonResponse({'error': 'Script execution failed.', 'details': result.stderr}, status=500)

        logger.info(f'Script executed successfully: {result.stdout}')
        return JsonResponse({'message': 'Success', 'details': result.stdout})

    except Exception as e:
        logger.exception("Error handling the request.")
        return JsonResponse({'error': 'Internal Server Error', 'details': str(e)}, status=500)
