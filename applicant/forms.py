from django.forms import ModelForm
from .models import Competence


class CompetencesForm(ModelForm):
    class Meta:
        model = Competence
        fields = "__all__"