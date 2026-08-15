from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class TutorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_profile",
    )
    subject = models.CharField(max_length=120, blank=True)
    qualification = models.CharField(max_length=180, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    availability = models.CharField(max_length=180, blank=True)

    def clean(self):
        if self.user_id and getattr(self.user, "role", None) != "TUTOR":
            raise ValidationError("Only users with the Tutor role can have a tutor profile.")

    def __str__(self):
        name = self.user.get_full_name() or self.user.username
        return f"{name} - {self.subject or 'Tutor'}"
