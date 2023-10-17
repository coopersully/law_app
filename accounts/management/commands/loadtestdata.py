from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Call commands to create faux data in bulk'

    def handle(self, *args, **kwargs):
        os.system('python manage.py loadtestprograms')
        os.system('python manage.py loadtestusers')
        os.system('python manage.py loadtestannouncements')
        os.system('python manage.py loadtestevents')