from django.urls import path

from . import views

app_name = "tutors"

urlpatterns = [
    path("", views.tutor_list, name="list"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("<int:pk>/", views.tutor_detail, name="detail"),
]
