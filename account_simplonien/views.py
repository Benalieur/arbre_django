from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render

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