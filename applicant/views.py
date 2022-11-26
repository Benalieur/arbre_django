from django.shortcuts import get_object_or_404, render
from applicant.models import Applicant


def index (request):
    return render(request, "applicant/index.html")

def applicants (request):
    applicants = Applicant.objects.all()
    return render(request, "applicant/applicants.html", context={"applicant":applicants})

def applicant_detail (request, slug):
    applicant_slug = get_object_or_404(Applicant, slug=slug)
    return render(request, "applicant/detail.html", context={"applicant":applicant_slug})
