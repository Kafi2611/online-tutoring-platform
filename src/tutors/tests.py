from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from .models import TutorProfile


class TutorSearchTests(TestCase):
    def setUp(self):
        tutor = User.objects.create_user(
            username="math_tutor",
            email="math@example.com",
            password="StrongPass123!",
            role=User.Role.TUTOR,
        )
        TutorProfile.objects.create(user=tutor, subject="Mathematics", qualification="B.Sc.")

    def test_search_by_subject(self):
        response = self.client.get(reverse("tutors:list"), {"q": "Math"})
        self.assertContains(response, "Mathematics")
