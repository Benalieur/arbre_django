from django.db import models
from django.urls import reverse


'''
Class des simploniens :
Photo
Nom
Prénom
nom_url
Poste recherché
Description
'''
class Applicant(models.Model):
    img=models.ImageField(upload_to="img_applicant")
    name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100)
    position=models.CharField(max_length=50, blank=True)
    description=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("applicant", kwargs={"slug": self.slug})
    

# iterable
COMP_CHOICES =(
	("1", 1),
	("2", 2),
	("3", 3),
)

# creating a form
class Competence(models.Model):
        C1=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C2=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C3=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C4=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C5=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C6=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C7=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C8=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C9=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C10=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C11=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C12=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C13=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C14=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C15=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C16=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C17=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
        C18=models.CharField(max_length=1, choices = COMP_CHOICES, default=1)
