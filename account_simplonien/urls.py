from django.urls import path
from .views import *


urlpatterns = [
    path('signup_simplonien/', SignupPage.as_view(), name='signup_simplonien'),
]
