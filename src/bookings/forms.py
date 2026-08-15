from django import forms
from django.utils import timezone

from .models import TutoringRequest


class TutoringRequestForm(forms.ModelForm):
    class Meta:
        model = TutoringRequest
        fields = ("subject", "preferred_date", "preferred_time", "message")
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "preferred_time": forms.TimeInput(attrs={"type": "time"}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data["preferred_date"]
        if preferred_date < timezone.localdate():
            raise forms.ValidationError("Preferred date cannot be in the past.")
        return preferred_date
