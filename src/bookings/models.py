from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class TutoringRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_tutoring_requests",
    )
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_tutoring_requests",
    )
    subject = models.CharField(max_length=120)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        if self.student_id and getattr(self.student, "role", None) != "STUDENT":
            raise ValidationError("The requester must have the Student role.")
        if self.tutor_id and getattr(self.tutor, "role", None) != "TUTOR":
            raise ValidationError("The selected tutor must have the Tutor role.")
        if self.student_id and self.tutor_id and self.student_id == self.tutor_id:
            raise ValidationError("A user cannot request a tutoring session from themselves.")

    def __str__(self):
        return f"{self.student} -> {self.tutor}: {self.subject} ({self.get_status_display()})"
