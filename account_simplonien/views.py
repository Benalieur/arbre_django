from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render


from django.views.generic import CreateView                             # For SignUp form Page  
from . import forms                                                     # For SignUp form Page 
from django.urls import reverse_lazy                                    # For signUp page methode 2
from django.contrib.auth.decorators import login_required



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
    return render(request, "account_simplonien/apply.html")


    #################################################################################################################################
#################################################################################################################################
#################################################################################################################################
###                                                                                                                           ###
###                                                     SignUp form Page                                                      ###
###                                                                                                                           ###
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'account_simplonien/signup.html'

