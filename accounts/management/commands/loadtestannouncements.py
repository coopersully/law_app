from django.core.management.base import BaseCommand

from announcements.models import Announcement


class Command(BaseCommand):
    help = 'Create faux announcement data in bulk'

    def handle(self, *args, **kwargs):
        announcements = [
            {
                'title': 'Welcome to the Law School Hub!',
                'content': 'We are excited to introduce the Law School Hub, your one-stop destination for staying '
                           'connected with the legal community. Explore our features and engage with fellow law '
                           'students from around the world. (Part of Program 1)',
                'program': 1
            },
            {
                'title': 'Upcoming Webinar on Constitutional Law',
                'content': 'Join us for an insightful webinar on Constitutional Law, featuring renowned legal '
                           'scholars. Don\'t miss this opportunity to deepen your understanding of constitutional '
                           'principles. (Part of Program 1)',
                'program': 1
            },
            {
                'title': 'New Chat Feature Now Available!',
                'content': 'We\'ve added a new chat feature to enhance communication among law students. Start '
                           'conversations, collaborate on projects, and build a stronger legal network. (Part of Program 1)',
                'program': 1
            },
            {
                'title': 'Important Announcement: Exam Schedule',
                'content': 'The fall semester exam schedule has been released. Please check the "Events" section for '
                           'details on exam dates, times, and locations. (Part of Program 2)',
                'program': 2
            },
            {
                'title': 'Legal Internship Opportunities',
                'content': 'Explore a variety of legal internship opportunities available for law students. Visit the '
                           '"Announcements" section for the latest updates on internships with prestigious law firms. (Part of Program 2)',
                'program': 2
            }
        ]

        for announcement_data in announcements:
            Announcement.objects.create(
                title=announcement_data['title'],
                content=announcement_data['content'],
                program_id=announcement_data['program']
            )

        # Output success message
        self.stdout.write(self.style.SUCCESS('Successfully created announcements.'))
