from django.urls import path

from . import views

app_name = "bookings"

urlpatterns = [
    path("new/<int:tutor_id>/", views.create_request, name="create"),
    path("student/", views.student_dashboard, name="student_dashboard"),
    path("tutor/", views.tutor_dashboard, name="tutor_dashboard"),
    path("<int:pk>/status/", views.update_status, name="update_status"),
    path("<int:pk>/cancel/", views.cancel_request, name="cancel"),
]
