from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.decorators import role_required
from accounts.models import User
from tutors.models import TutorProfile

from .forms import TutoringRequestForm
from .models import TutoringRequest


@role_required(User.Role.STUDENT)
def create_request(request, tutor_id):
    tutor = get_object_or_404(User, pk=tutor_id, role=User.Role.TUTOR)
    tutor_profile = TutorProfile.objects.filter(user=tutor).first()
    initial = {"subject": tutor_profile.subject if tutor_profile else ""}

    if request.method == "POST":
        form = TutoringRequestForm(request.POST)
        if form.is_valid():
            tutoring_request = form.save(commit=False)
            tutoring_request.student = request.user
            tutoring_request.tutor = tutor
            tutoring_request.status = TutoringRequest.Status.PENDING
            tutoring_request.save()
            messages.success(request, "Tutoring request sent successfully.")
            return redirect("bookings:student_dashboard")
    else:
        form = TutoringRequestForm(initial=initial)

    return render(
        request,
        "bookings/request_form.html",
        {"form": form, "tutor": tutor, "tutor_profile": tutor_profile},
    )


@role_required(User.Role.STUDENT)
def student_dashboard(request):
    requests = TutoringRequest.objects.filter(student=request.user).select_related("tutor")
    return render(request, "bookings/student_dashboard.html", {"requests": requests})


@role_required(User.Role.TUTOR)
def tutor_dashboard(request):
    requests = TutoringRequest.objects.filter(tutor=request.user).select_related("student")
    return render(request, "bookings/tutor_dashboard.html", {"requests": requests})


@require_POST
@role_required(User.Role.TUTOR)
def update_status(request, pk):
    tutoring_request = get_object_or_404(TutoringRequest, pk=pk, tutor=request.user)
    action = request.POST.get("action")

    if tutoring_request.status != TutoringRequest.Status.PENDING:
        messages.error(request, "Only pending requests can be accepted or rejected.")
        return redirect("bookings:tutor_dashboard")

    if action == "accept":
        tutoring_request.status = TutoringRequest.Status.ACCEPTED
        messages.success(request, "Request accepted.")
    elif action == "reject":
        tutoring_request.status = TutoringRequest.Status.REJECTED
        messages.success(request, "Request rejected.")
    else:
        messages.error(request, "Unknown request action.")
        return redirect("bookings:tutor_dashboard")

    tutoring_request.save(update_fields=["status"])
    return redirect("bookings:tutor_dashboard")


@require_POST
@role_required(User.Role.STUDENT)
def cancel_request(request, pk):
    tutoring_request = get_object_or_404(TutoringRequest, pk=pk, student=request.user)

    if tutoring_request.status == TutoringRequest.Status.PENDING:
        tutoring_request.status = TutoringRequest.Status.CANCELLED
        tutoring_request.save(update_fields=["status"])
        messages.success(request, "Request cancelled.")
    else:
        messages.error(request, "Only pending requests can be cancelled.")

    return redirect("bookings:student_dashboard")
