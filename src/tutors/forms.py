from django import forms

from .models import TutorProfile


class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ("subject", "qualification", "experience_years", "bio", "availability")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 5}),
        }
