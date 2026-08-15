from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import role_required
from accounts.models import User

from .forms import TutorProfileForm
from .models import TutorProfile


def tutor_list(request):
    query = request.GET.get("q", "").strip()
    tutors = TutorProfile.objects.select_related("user").exclude(subject="").order_by("user__first_name", "user__username")

    if query:
        tutors = tutors.filter(
            Q(subject__icontains=query)
            | Q(user__username__icontains=query)
            | Q(user__first_name__icontains=query)
            | Q(user__last_name__icontains=query)
        )

    return render(request, "tutors/tutor_list.html", {"tutors": tutors, "query": query})


def tutor_detail(request, pk):
    profile = get_object_or_404(TutorProfile.objects.select_related("user"), pk=pk)
    return render(request, "tutors/tutor_detail.html", {"profile": profile})


@role_required(User.Role.TUTOR)
def profile_edit(request):
    profile, _ = TutorProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = TutorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Tutor profile saved.")
            return redirect("tutors:detail", pk=profile.pk)
    else:
        form = TutorProfileForm(instance=profile)

    return render(request, "tutors/profile_form.html", {"form": form, "profile": profile})
