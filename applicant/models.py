from django.db import models
from django.urls import reverse

'''
Photo
Nom / Prénom
Poste recherché
Description

'''


class Applicant(models.Model):
    img=models.ImageField(upload_to="img_applicant", blank=True, null=True)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    position=models.CharField(max_length=50)
    description=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("applicant", kwargs={"slug": self.slug})
    
    