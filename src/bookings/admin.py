from django.contrib import admin

from .models import TutoringRequest


@admin.register(TutoringRequest)
class TutoringRequestAdmin(admin.ModelAdmin):
    list_display = ("student", "tutor", "subject", "preferred_date", "status", "created_at")
    list_filter = ("status", "preferred_date")
    search_fields = ("student__username", "tutor__username", "subject")
