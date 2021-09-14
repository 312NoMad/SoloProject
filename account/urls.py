from django.urls import path

from .views import *


urlpatterns = [
    path('', LogoutView),
    path('', LoginView),
    path('', ActivationView),
    path('', ChangePasswordView),
    path('', ForgotPasswordView),
    path('', RegistrationView),
]
