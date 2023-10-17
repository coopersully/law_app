from django.core.management.base import BaseCommand

from agenda.models import Event


class Command(BaseCommand):
    help = 'Create faux event data in bulk'

    def handle(self, *args, **kwargs):
        events = [
            {
                'title': 'Law Seminar: Cybersecurity in the Digital Age',
                'description': 'Join us for an engaging seminar on cybersecurity and its legal implications in the digital age. Expert speakers will discuss data privacy, cyber threats, and legal strategies to protect businesses.',
                'location': 'Samford University Law School Auditorium',
                'datetime': '2023-10-15 14:00:00',
                'map': 'https://maps.app.goo.gl/xNCshWcreRHSwUC59'
            },
            {
                'title': 'Mock Trial Competition',
                'description': 'Participate in our annual Mock Trial Competition and showcase your advocacy skills. This event provides an excellent opportunity to gain courtroom experience and network with legal professionals.',
                'location': 'Mock Trial Courtroom, Law Building',
                'datetime': '2023-11-05 09:30:00',
                'map': 'https://maps.app.goo.gl/xNCshWcreRHSwUC59'
            },
            {
                'title': 'Legal Tech Workshop: AI in Law',
                'description': 'Discover the latest trends in legal technology and artificial intelligence. Learn how AI is revolutionizing the legal field and attend hands-on workshops with AI tools used in the industry.',
                'location': 'Law School Conference Room',
                'datetime': '2023-11-20 16:00:00',
                'map': 'https://maps.app.goo.gl/xNCshWcreRHSwUC59'
            },
            {
                'title': 'Moot Court Competition Finals',
                'description': 'Witness the final round of our Moot Court Competition. Top students will argue a complex case before a panel of judges. Attend and support your peers in this prestigious event.',
                'location': 'Moot Courtroom, Law Building',
                'datetime': '2023-12-10 13:00:00',
                'map': 'https://maps.app.goo.gl/xNCshWcreRHSwUC59'
            },
        ]

        for event_data in events:
            Event.objects.create(
                title=event_data['title'],
                description=event_data['description'],
                location=event_data['location'],
                datetime=event_data['datetime'],
                map=event_data['map'],
                owner_id=1,
                program_id=1
            )