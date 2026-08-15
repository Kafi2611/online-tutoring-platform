from django.test import TestCase
from django.urls import reverse

from .models import User


class RegistrationTests(TestCase):
    def test_student_registration(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "student1",
                "first_name": "Student",
                "last_name": "One",
                "email": "student1@example.com",
                "role": User.Role.STUDENT,
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("accounts:dashboard"),
            fetch_redirect_response=False,
        )

        self.assertTrue(
            User.objects.filter(
                username="student1",
                role=User.Role.STUDENT
            ).exists()
        )