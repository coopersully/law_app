from django.core.management.base import BaseCommand

from accounts.models import Program


class Command(BaseCommand):
    help = 'Create faux announcement data in bulk'

    def handle(self, *args, **kwargs):
        programs = [
            {'title':'Cambridge!',
             'location': 'Cambridge, GB',
             'year': 2024},
            {'title':'Scotland!',
             'location': 'Edinburgh, GB',
             'year': 2024}
        ]

        for program_data in programs:
            Program.objects.create(
                title=program_data['title'],
                location=program_data['location'],
                year=program_data['year'],
            )

        # Output success message
        self.stdout.write(self.style.SUCCESS('Successfully created test programs.'))
