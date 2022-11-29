"""Arbre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from Arbre import settings

from applicant.views import applicant_detail, index, applicants
from account_simplonien.views import signup_simplonien, logout_simplonien, login_simplonien, account, apply


urlpatterns = [
    path('', index, name="index_page"),
    path('admin/', admin.site.urls),
    path('login/', login_simplonien, name="login"),
    path('logout/', logout_simplonien, name="logout"),
    path('account/', account, name="account"),
    path('apply/', apply, name="apply"),
    # path('signup_simplonien/', signup_simplonien, name="signup_simplonien"),
    path('candidats/', applicants, name="applicants_page"),
    path('candidats/<str:slug>', applicant_detail, name="applicant"),
    path('', include("account_simplonien.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
