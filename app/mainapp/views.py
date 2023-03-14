from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render
from rest_framework.viewsets import ModelViewSet
from .models import Idea
from .serializers import IdeaModelSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IdeaModelViewSet(ModelViewSet):

    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer


def ideas_list(request): # список всех идей.
    title = "Идеи"

    ideas = Idea.objects.all()

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "mainapp/ideas_list.html", content)


def idea_add(request): # добавление идеи через форму

    if request.method == 'POST':
        username = request.user.username

        title = request.POST['title']
        rubrics = request.POST['rubrics']
        preview = request.POST['preview']
        body = request.POST['body']
        if title and rubrics and preview and body: # проверка наличия данных во всех полях

            new_idea = Idea.objects.create(autor=username, title=title, rubrics=rubrics,
                                           preview=preview, body=body)
            new_idea.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def idea_edit(request, pk): # изменение идеи через форму

    if request.method == 'POST':

        idea = Idea.objects.filter(pk=pk).first()

        # проверка на наличие ввода в поля. есть данные, то изменяет, если нет то пропускает

        title = request.POST['title-edit']
        if title: idea.title = title

        rubrics = request.POST['rubrics-edit']
        if rubrics: idea.rubrics = rubrics

        preview = request.POST['preview-edit']
        if preview: idea.preview = preview

        body = request.POST['body-edit']
        if body: idea.body = body

        idea.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def idea_delete(request, pk): # удаление идеи при нажатии на кнопку

    idea = Idea.objects.filter(pk=pk)
    idea.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
