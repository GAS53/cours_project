from django.urls import path
from django.views.generic import RedirectView
import authapp.views as authapp

app_name = "authapp"

urlpatterns = [
    path("", RedirectView.as_view(url="login")),
    path("login/", authapp.login, name="login"),
    path("logout/", authapp.logout, name="logout"),
    path("register/", authapp.register, name="register"),
    path("edit/", authapp.edit, name="edit"),
]
