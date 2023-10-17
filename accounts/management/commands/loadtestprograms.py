from django.core.management.base import BaseCommand

from accounts.models import Program


class Command(BaseCommand):
    help = 'Create faux announcement data in bulk'

    def handle(self, *args, **kwargs):
        programs = [
            {'title':'Cambridge!',
             'year': 2024},
            {'title':'Scotland!',
             'year': 2024}
        ]

        for program_data in programs:
            Program.objects.create(
                title=program_data['title'],
                year=program_data['year'],
            )
