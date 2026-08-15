from django.contrib import admin

from .models import TutorProfile


@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "subject", "qualification", "experience_years")
    search_fields = ("user__username", "user__first_name", "user__last_name", "subject")
