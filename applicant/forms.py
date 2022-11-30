from django.forms import ModelForm
from .models import CompForm


class CompetencesForm(ModelForm):
    class Meta:
        form = CompForm
        fields = ("C1", "C1", "C1", "C1", "C1", "C1", "C1", "C1", "C1", "C1", "C1", "C1", )