from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authnapp.forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm


def login(request):
    title = "вход"

    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)

            """ тут програма при авторизации перемещает в кабинет. это тестовая ссылка, её можно изменить на другую,
            например, главную страницу """

            return cabinet(request)

    content = {"title": title, "login_form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = ShopUserRegisterForm()

    content = {"title": title, "register_form": register_form}
    return render(request, "authnapp/register.html", content)


def cabinet(request):
    title = "Кабинет"
    
    #тестовая

    name = request.user.username

    content = {"title": title, "name": name}
    return render(request, "authnapp/cabinet.html", content)

