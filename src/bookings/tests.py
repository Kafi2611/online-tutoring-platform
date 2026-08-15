from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from .models import TutoringRequest


class BookingFlowTests(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(
            username="student",
            email="student@example.com",
            password="StrongPass123!",
            role=User.Role.STUDENT,
        )
        self.tutor = User.objects.create_user(
            username="tutor",
            email="tutor@example.com",
            password="StrongPass123!",
            role=User.Role.TUTOR,
        )

    def test_tutor_can_accept_pending_request(self):
        request_obj = TutoringRequest.objects.create(
            student=self.student,
            tutor=self.tutor,
            subject="Programming",
            preferred_date=timezone.localdate() + timedelta(days=1),
            preferred_time="19:00",
        )
        self.client.force_login(self.tutor)
        response = self.client.post(
            reverse("bookings:update_status", args=[request_obj.pk]),
            {"action": "accept"},
        )
        self.assertRedirects(response, reverse("bookings:tutor_dashboard"))
        request_obj.refresh_from_db()
        self.assertEqual(request_obj.status, TutoringRequest.Status.ACCEPTED)
