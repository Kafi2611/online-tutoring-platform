from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from accounts.models import User
from bookings.models import TutoringRequest
from tutors.models import TutorProfile


class Command(BaseCommand):
    help = "Create small demo data for the Online Tutoring Platform MVP."

    def handle(self, *args, **options):
        demo_password = "demo12345"

        student, _ = User.objects.get_or_create(
            username="student_demo",
            defaults={
                "first_name": "Demo",
                "last_name": "Student",
                "email": "student_demo@example.com",
                "role": User.Role.STUDENT,
            },
        )
        student.email = "student_demo@example.com"
        student.role = User.Role.STUDENT
        student.set_password(demo_password)
        student.save()

        tutor_math, _ = User.objects.get_or_create(
            username="tutor_math",
            defaults={
                "first_name": "Nadia",
                "last_name": "Rahman",
                "email": "tutor_math@example.com",
                "role": User.Role.TUTOR,
            },
        )
        tutor_math.email = "tutor_math@example.com"
        tutor_math.role = User.Role.TUTOR
        tutor_math.set_password(demo_password)
        tutor_math.save()
        TutorProfile.objects.update_or_create(
            user=tutor_math,
            defaults={
                "subject": "Mathematics",
                "qualification": "B.Sc. in Mathematics",
                "experience_years": 3,
                "bio": "Friendly tutor focused on algebra, calculus, and exam preparation.",
                "availability": "Sun-Tue, 6:00 PM-9:00 PM",
            },
        )

        tutor_cse, _ = User.objects.get_or_create(
            username="tutor_cse",
            defaults={
                "first_name": "Arif",
                "last_name": "Hasan",
                "email": "tutor_cse@example.com",
                "role": User.Role.TUTOR,
            },
        )
        tutor_cse.email = "tutor_cse@example.com"
        tutor_cse.role = User.Role.TUTOR
        tutor_cse.set_password(demo_password)
        tutor_cse.save()
        TutorProfile.objects.update_or_create(
            user=tutor_cse,
            defaults={
                "subject": "Programming",
                "qualification": "B.Sc. in Computer Science & Engineering",
                "experience_years": 2,
                "bio": "Tutoring Python, programming fundamentals, data structures, and algorithms.",
                "availability": "Thu-Sat, 7:00 PM-10:00 PM",
            },
        )

        tomorrow = timezone.localdate() + timedelta(days=2)
        TutoringRequest.objects.get_or_create(
            student=student,
            tutor=tutor_math,
            preferred_date=tomorrow,
            preferred_time="18:30",
            defaults={
                "subject": "Calculus",
                "message": "I need help understanding differentiation before my class test.",
                "status": TutoringRequest.Status.PENDING,
            },
        )

        self.stdout.write(self.style.SUCCESS("Demo data is ready."))
        self.stdout.write("student_demo / demo12345")
        self.stdout.write("tutor_math / demo12345")
        self.stdout.write("tutor_cse / demo12345")
