from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from .forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm
from rest_framework.viewsets import ModelViewSet
from .models import ShopUser
from .serializers import ShopUserModelSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class ShopUserModelViewSet(ModelViewSet):

    queryset = ShopUser.objects.all()
    serializer_class = ShopUserModelSerializer


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

    name = request.user.username

    content = {"title": title, "name": name}
    return render(request, "authnapp/cabinet.html", content)



def edit(request):
    title = "редактирование"

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "authnapp/edit.html", content)
