import random

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Create faux user data in bulk'

    def handle(self, *args, **kwargs):
        CustomUser.objects.create_user(username="atalanta.blalock", email="me@example.com", first_name="Atalanta",
                                       last_name="Blalock", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="ablalock@campbell.edu", student_id=4587)

        CustomUser.objects.create_user(username="cherey.lancaster", email="me@example.com", first_name="Cherey",
                                       last_name="Lancaster", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="clancaster@campbell.edu", student_id=5927)

        CustomUser.objects.create_user(username="kyrstin.hall", email="me@example.com", first_name="Dr. Kyrstin",
                                       last_name="Hall", password="password", role="staff", phone_number="205-***-****",
                                       bio="I love law!", school_email="khall@samford.edu", student_id=1066)

        CustomUser.objects.create_user(username="astrid.justice", email="me@example.com", first_name="Dr. Astrid",
                                       last_name="Justice", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="ajustice@samford.edu", student_id=7938)

        CustomUser.objects.create_user(username="randi.may", email="me@example.com", first_name="Randi",
                                       last_name="May", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!", school_email="rmay@campbell.edu",
                                       student_id=8795)

        CustomUser.objects.create_user(username="sarena.shelton", email="me@example.com", first_name="Sarena",
                                       last_name="Shelton", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="sshelton@samford.edu", student_id=8489)

        CustomUser.objects.create_user(username="marrilee.jordan", email="me@example.com", first_name="Marrilee",
                                       last_name="Jordan", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="mjordan@samford.edu", student_id=7766)

        CustomUser.objects.create_user(username="albertine.norman", email="me@example.com", first_name="Dr. Albertine",
                                       last_name="Norman", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="anorman@samford.edu", student_id=2626)

        CustomUser.objects.create_user(username="mimi.high", email="me@example.com", first_name="Mimi",
                                       last_name="High", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!", school_email="mhigh@samford.edu",
                                       student_id=4358)

        CustomUser.objects.create_user(username="hallie.huffman", email="me@example.com", first_name="Hallie",
                                       last_name="Huffman", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="hhuffman@samford.edu", student_id=5378)

        CustomUser.objects.create_user(username="vivianne.blackwell", email="me@example.com", first_name="Vivianne",
                                       last_name="Blackwell", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="vblackwell@campbell.edu", student_id=5432)

        CustomUser.objects.create_user(username="sarah.poole", email="me@example.com", first_name="Sarah",
                                       last_name="Poole", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="spoole@samford.edu", student_id=8105)

        CustomUser.objects.create_user(username="merrie.batchelor", email="me@example.com", first_name="Dr. Merrie",
                                       last_name="Batchelor", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="mbatchelor@campbell.edu", student_id=7830)

        CustomUser.objects.create_user(username="alidia.oh", email="me@example.com", first_name="Alidia",
                                       last_name="Oh", password="password", role="faculty", phone_number="205-***-****",
                                       bio="I love law!", school_email="aoh@samford.edu", student_id=5779)

        CustomUser.objects.create_user(username="fanny.collier", email="me@example.com", first_name="Fanny",
                                       last_name="Collier", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="fcollier@campbell.edu", student_id=6265)

        CustomUser.objects.create_user(username="fan.burton", email="me@example.com", first_name="Fan",
                                       last_name="Burton", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="fburton@samford.edu", student_id=145)

        CustomUser.objects.create_user(username="dorette.beasley", email="me@example.com", first_name="Dorette",
                                       last_name="Beasley", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="dbeasley@samford.edu", student_id=7242)

        CustomUser.objects.create_user(username="dalia.kaplan", email="me@example.com", first_name="Dalia",
                                       last_name="Kaplan", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="dkaplan@campbell.edu", student_id=4232)

        CustomUser.objects.create_user(username="vivyan.riley", email="me@example.com", first_name="Vivyan",
                                       last_name="Riley", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="vriley@campbell.edu", student_id=2024)

        CustomUser.objects.create_user(username="fayina.brandon", email="me@example.com", first_name="Fayina",
                                       last_name="Brandon", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="fbrandon@samford.edu", student_id=5658)

        CustomUser.objects.create_user(username="eunice.creech", email="me@example.com", first_name="Dr. Eunice",
                                       last_name="Creech", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="ecreech@samford.edu", student_id=743)

        CustomUser.objects.create_user(username="gerianna.field", email="me@example.com", first_name="Dr. Gerianna",
                                       last_name="Field", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="gfield@samford.edu", student_id=3201)

        CustomUser.objects.create_user(username="george.stokes", email="me@example.com", first_name="George",
                                       last_name="Stokes", password="password", role="student",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="gstokes@campbell.edu", student_id=1657)

        CustomUser.objects.create_user(username="alexina.keith", email="me@example.com", first_name="Dr. Alexina",
                                       last_name="Keith", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="akeith@campbell.edu", student_id=6100)

        CustomUser.objects.create_user(username="sofia.allred", email="me@example.com", first_name="Sofia",
                                       last_name="Allred", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="sallred@campbell.edu", student_id=4295)

        CustomUser.objects.create_user(username="maure.barber", email="me@example.com", first_name="Maure",
                                       last_name="Barber", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="mbarber@campbell.edu", student_id=1266)

        CustomUser.objects.create_user(username="jamie.cline", email="me@example.com", first_name="Jamie",
                                       last_name="Cline", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="jcline@campbell.edu", student_id=1599)

        CustomUser.objects.create_user(username="aloisia.archer", email="me@example.com", first_name="Aloisia",
                                       last_name="Archer", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="aarcher@campbell.edu", student_id=1407)

        CustomUser.objects.create_user(username="jacquetta.bailey", email="me@example.com", first_name="Dr. Jacquetta",
                                       last_name="Bailey", password="password", role="staff",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="jbailey@samford.edu", student_id=2681)

        CustomUser.objects.create_user(username="anabel.duncan", email="me@example.com", first_name="Anabel",
                                       last_name="Duncan", password="password", role="faculty",
                                       phone_number="205-***-****", bio="I love law!",
                                       school_email="aduncan@samford.edu", student_id=6556)