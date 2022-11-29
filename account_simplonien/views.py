from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render
from applicant.models import Applicant
from django.core.files.storage import FileSystemStorage


User = get_user_model()

# Vue d'inscription
def signup_simplonien(request):
    if request.method == "POST":
        #Traiter le formulaire
        username =request.POST.get("username")
        password =request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("../")

    return render(request, "account_simplonien/signup.html")


# Vue de connexion
def login_simplonien(request):
    if request.method == "POST":
        #connecte l'utilisateur
        username =request.POST.get("username")
        password =request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("../")

    return render(request, "account_simplonien/login.html")

# Vue de déconnexion
def logout_simplonien(request):
    logout(request)
    return redirect("../")

# Vue du profil utilisateur simplonien
def account(request):
    return render(request, "account_simplonien/account.html")

# Vue pour la candidature du simplonien
def apply(request):
    if request.method == "POST":

        name =request.POST.get("name")
        first_name =request.POST.get("first_name")
        slug =request.POST.get("slug")
        position =request.POST.get("position")
        description =request.POST.get("description")

        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(name + "_" + first_name+upload.name[len(upload.name)-4:], upload)
        file_url = fss.url(file)

        img = file_url
        
        applicant = Applicant(img=img, name=name, first_name=first_name, slug=slug, position=position, description=description)
        applicant.save()
    
    return render(request, "account_simplonien/apply.html")