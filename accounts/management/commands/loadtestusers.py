from django.core.management.base import BaseCommand

from accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Create faux user data in bulk'

    def handle(self, *args, **kwargs):
        user = [
            {
                'username': 'rosemary.wise',
                'email': 'rwise@samford.edu',
                'first_name': 'Rosemary',
                'last_name': 'Wise',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-777-9972',
                'bio': 'I love law!',
                'school_email': 'rwise@samford.edu',
                'student_id': 5142,
                'program_id': 2
            },
            {
                'username': 'ara.mckinney',
                'email': 'amckinney@samford.edu',
                'first_name': 'Dr. Ara',
                'last_name': 'McKinney',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-555-1235',
                'bio': 'I love law!',
                'school_email': 'amckinney@samford.edu',
                'student_id': 9717,
                'program_id': 2
            },
            {
                'username': 'samara.mayer',
                'email': 'smayer@campbell.edu',
                'first_name': 'Dr. Samara',
                'last_name': 'Mayer',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-123-4335',
                'bio': 'I love law!',
                'school_email': 'smayer@campbell.edu',
                'student_id': 1878,
                'program_id': 2
            },
            {
                'username': 'carlie.banks',
                'email': 'cbanks@campbell.edu',
                'first_name': 'Dr. Carlie',
                'last_name': 'Banks',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-234-3254',
                'bio': 'I love law!',
                'school_email': 'cbanks@campbell.edu',
                'student_id': 8216,
                'program_id': 1
            },
            {
                'username': 'aryn.lowry',
                'email': 'alowry@samford.edu',
                'first_name': 'Aryn',
                'last_name': 'Lowry',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-333-2134',
                'bio': 'I love law!',
                'school_email': 'alowry@samford.edu',
                'student_id': 3221,
                'program_id': 2
            },
            {
                'username': 'iormina.tucker',
                'email': 'itucker@samford.edu',
                'first_name': 'Iormina',
                'last_name': 'Tucker',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-009-8888',
                'bio': 'I love law!',
                'school_email': 'itucker@samford.edu',
                'student_id': 542,
                'program_id': 1
            },
            {
                'username': 'lurlene.ivey',
                'email': 'livey@samford.edu',
                'first_name': 'Lurlene',
                'last_name': 'Ivey',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-112-9976',
                'bio': 'I love law!',
                'school_email': 'livey@samford.edu',
                'student_id': 4757,
                'program_id': 2
            },
            {
                'username': 'terry.desai',
                'email': 'tdesai@campbell.edu',
                'first_name': 'Terry',
                'last_name': 'Desai',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-4457-4442',
                'bio': 'I love law!',
                'school_email': 'tdesai@campbell.edu',
                'student_id': 3595,
                'program_id': 1
            },
            {
                'username': 'cora.buck',
                'email': 'cbuck@campbell.edu',
                'first_name': 'Dr. Cora',
                'last_name': 'Buck',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-445-2234',
                'bio': 'I love law!',
                'school_email': 'cbuck@campbell.edu',
                'student_id': 7251,
                'program_id': 1
            },
            {
                'username': 'de.horn',
                'email': 'dhorn@samford.edu',
                'first_name': 'Dr. De',
                'last_name': 'Horn',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-900-2345',
                'bio': 'I love law!',
                'school_email': 'dhorn@samford.edu',
                'student_id': 6977,
                'program_id': 2
            },
            {
                'username': 'almeta.nixon',
                'email': 'anixon@samford.edu',
                'first_name': 'Dr. Almeta',
                'last_name': 'Nixon',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-446-8875',
                'bio': 'I love law!',
                'school_email': 'anixon@samford.edu',
                'student_id': 7207,
                'program_id': 2
            },
            {
                'username': 'anabel.cannon',
                'email': 'acannon@campbell.edu',
                'first_name': 'Anabel',
                'last_name': 'Cannon',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-332-1146',
                'bio': 'I love law!',
                'school_email': 'acannon@campbell.edu',
                'student_id': 703,
                'program_id': 1
            },
            {
                'username': 'chastity.hatcher',
                'email': 'chatcher@campbell.edu',
                'first_name': 'Chastity',
                'last_name': 'Hatcher',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-113-4412',
                'bio': 'I love law!',
                'school_email': 'chatcher@campbell.edu',
                'student_id': 695,
                'program_id': 2
            },
            {
                'username': 'davida.kahn',
                'email': 'dkahn@samford.edu',
                'first_name': 'Dr. Davida',
                'last_name': 'Kahn',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-099-4432',
                'bio': 'I love law!',
                'school_email': 'dkahn@samford.edu',
                'student_id': 7266,
                'program_id': 1
            },
            {
                'username': 'lilith.hinson',
                'email': 'lhinson@samford.edu',
                'first_name': 'Lilith',
                'last_name': 'Hinson',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-345-4446',
                'bio': 'I love law!',
                'school_email': 'lhinson@samford.edu',
                'student_id': 128,
                'program_id': 2
            },
            {
                'username': 'anne-corinne.shields',
                'email': 'ashields@campbell.edu',
                'first_name': 'Anne-Corinne',
                'last_name': 'Shields',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-445-5678',
                'bio': 'I love law!',
                'school_email': 'ashields@campbell.edu',
                'student_id': 5890,
                'program_id': 2
            },
            {
                'username': 'andriana.ferrell',
                'email': 'aferrell@samford.edu',
                'first_name': 'Andriana',
                'last_name': 'Ferrell',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-997-3345',
                'bio': 'I love law!',
                'school_email': 'aferrell@samford.edu',
                'student_id': 3728,
                'program_id': 1
            },
            {
                'username': 'elyse.callahan',
                'email': 'ecallahan@samford.edu',
                'first_name': 'Dr. Elyse',
                'last_name': 'Callahan',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-123-9987',
                'bio': 'I love law!',
                'school_email': 'ecallahan@samford.edu',
                'student_id': 3044,
                'program_id': 2
            },
            {
                'username': 'teddie.weiner',
                'email': 'tweiner@campbell.edu',
                'first_name': 'Teddie',
                'last_name': 'Weiner',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-087-8665',
                'bio': 'I love law!',
                'school_email': 'tweiner@campbell.edu',
                'student_id': 9358,
                'program_id': 1
            },
            {
                'username': 'carri.camp',
                'email': 'ccamp@campbell.edu',
                'first_name': 'Carri',
                'last_name': 'Camp',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-908-6789',
                'bio': 'I love law!',
                'school_email': 'ccamp@campbell.edu',
                'student_id': 3992,
                'program_id': 1
            },
            {
                'username': 'brittne.cook',
                'email': 'bcook@samford.edu',
                'first_name': 'Brittne',
                'last_name': 'Cook',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-976-4679',
                'bio': 'I love law!',
                'school_email': 'bcook@samford.edu',
                'student_id': 9860,
                'program_id': 2
            },
            {
                'username': 'winona.frost',
                'email': 'wfrost@samford.edu',
                'first_name': 'Dr. Winona',
                'last_name': 'Frost',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-976-9862',
                'bio': 'I love law!',
                'school_email': 'wfrost@samford.edu',
                'student_id': 7136,
                'program_id': 1
            },
            {
                'username': 'barb.currie',
                'email': 'bcurrie@samford.edu',
                'first_name': 'Barb',
                'last_name': 'Currie',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-991-1834',
                'bio': 'I love law!',
                'school_email': 'bcurrie@samford.edu',
                'student_id': 5987,
                'program_id': 1
            },
            {
                'username': 'madlen.galloway',
                'email': 'mgalloway@campbell.edu',
                'first_name': 'Madlen',
                'last_name': 'Galloway',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-245-0997',
                'bio': 'I love law!',
                'school_email': 'mgalloway@campbell.edu',
                'student_id': 251,
                'program_id': 1
            },
            {
                'username': 'adrea.bender',
                'email': 'abender@campbell.edu',
                'first_name': 'Adrea',
                'last_name': 'Bender',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-778-9876',
                'bio': 'I love law!',
                'school_email': 'abender@campbell.edu',
                'student_id': 5112,
                'program_id': 2
            },
            {
                'username': 'collette.franklin',
                'email': 'cfranklin@samford.edu',
                'first_name': 'Collette',
                'last_name': 'Franklin',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-664-3245',
                'bio': 'I love law!',
                'school_email': 'cfranklin@samford.edu',
                'student_id': 6994,
                'program_id': 1
            },
            {
                'username': 'genni.stark',
                'email': 'gstark@campbell.edu',
                'first_name': 'Dr. Genni',
                'last_name': 'Stark',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-432-3412',
                'bio': 'I love law!',
                'school_email': 'gstark@campbell.edu',
                'student_id': 6589,
                'program_id': 2
            },
            {
                'username': 'nani.goldstein',
                'email': 'ngoldstein@samford.edu',
                'first_name': 'Nani',
                'last_name': 'Goldstein',
                'password': 'password',
                'role': 'student',
                'phone_number': '205-555-4323',
                'bio': 'I love law!',
                'school_email': 'ngoldstein@samford.edu',
                'student_id': 908,
                'program_id': 1
            },
            {
                'username': 'amberly.wiggins',
                'email': 'awiggins@campbell.edu',
                'first_name': 'Dr. Amberly',
                'last_name': 'Wiggins',
                'password': 'password',
                'role': 'staff',
                'phone_number': '205-069-49342',
                'bio': 'I love law!',
                'school_email': 'awiggins@campbell.edu',
                'student_id': 6262,
                'program_id': 2
            },
            {
                'username': 'farica.cole',
                'email': 'fcole@samford.edu',
                'first_name': 'Farica',
                'last_name': 'Cole',
                'password': 'password',
                'role': 'faculty',
                'phone_number': '205-423-1235',
                'bio': 'I love law!',
                'school_email': 'fcole@samford.edu',
                'student_id': 2343,
                'program_id': 1
            }
        ]

        for user_data in user:
            CustomUser.objects.create_user(username=user_data['username'], email=user_data['email'], first_name=user_data['first_name'],
                                           last_name=user_data['last_name'], password=user_data['password'], role=user_data['role'],
                                           phone_number=user_data['phone_number'], bio=user_data['bio'],school_email=user_data['school_email'],
                                           student_id=user_data['student_id'], program_id=user_data['program_id'])

        # Output success message
        self.stdout.write(self.style.SUCCESS('Successfully created test users.'))
