from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render
from rest_framework.viewsets import ModelViewSet
from .models import Idea, Feedback
from .serializers import IdeaModelSerializer, FeedbackModelSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IdeaModelViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer


class FeedbackModelViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackModelSerializer


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


""" html форм для изменения и удаления отзывов пока нет. но они работают так же как идеи. """


def feedback_add(request, pk): # добавление отзыва через форму

    if request.method == 'POST':

        idea = Idea.objects.filter(pk=pk).first()

        rating = request.POST['rating']
        feedback = request.POST['feedback']

        new_feedback = Feedback.objects.create(idea=idea, rating=rating, feedback=feedback)
        new_feedback.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def feedback_edit(request, pk): # изменение отзыва через форму

    if request.method == 'POST':

        idea = Idea.objects.filter(pk=pk).first()

        # проверка на наличие ввода в поля. есть данные, то изменяет, если нет то пропускает

        rating = request.POST['rating-edit']
        if rating: idea.title = rating

        feedback = request.POST['feedback-edit']
        if feedback: idea.feedback = feedback

        idea.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def feedback_delete(request, pk): # удаление отзыва при нажатии на кнопку

    feedback = Feedback.objects.filter(pk=pk)
    feedback.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

