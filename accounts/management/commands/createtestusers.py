import random

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from accounts.models import CustomUser
from faker import Faker


class Command(BaseCommand):
    help = 'Create faux user data in bulk'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']
        admin = kwargs['admin']

        for i in range(total):
            full_name = fake.name().split()
            first_name = full_name[0]
            last_name = ' '.join(full_name[1:])
            username = f"{first_name.lower()}.{last_name.lower()}"
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            school_email = f"{first_name[0].lower()}{last_name.lower()}@{random.choice(['samford','campbell'])}.edu"

            if admin:
                CustomUser.objects.create_superuser(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=get_random_string(length=12),
                    role='admin'
                )
            else:
                CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=get_random_string(length=12),
                    role=fake.random_element(['student', 'faculty', 'staff']),
                    phone_number=fake.phone_number(),
                    bio=fake.text(),
                    school_email=school_email,
                    student_id=fake.random_int(min=1000, max=9999)
                )
            self.stdout.write(self.style.SUCCESS('Successfully created new user'))
