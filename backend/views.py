from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render
from rest_framework.viewsets import ModelViewSet
from .models import Idea, Feedback, JoinedUsers, LikesToIdeas
from .serializers import IdeaModelSerializer, FeedbackModelSerializer, JoinedUsersModelSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView


class Temp(TemplateView):
    template_name = 'backend/index.html'


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IdeaModelViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer


class FeedbackModelViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackModelSerializer


class JoinedUsersModelViewSet(ModelViewSet):
    queryset = JoinedUsers.objects.all()
    serializer_class = JoinedUsersModelSerializer


""" идеи. добавление, удаление, изменение """


def main(request):  # список всех идей.
    title = "Идеи"

    ideas = Idea.objects.all()
    
    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "backend/index.html", content)


def search(request):
    if request.method == 'POST':
        title = "Поиск"
        name = request.POST['search']

        print(name)

        ideas = Idea.objects.all()
        ideas_list = []

        for idea in ideas:
            if name in idea.title:
                ideas_list.append(idea)

        content = {"title": title, "ideas": ideas_list}

        return render(request, "backend/index.html", content)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def my_ideas(request):
    title = "Профиль"
    ideas = Idea.objects.filter(autor=request.user.username)

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "backend/my_ideas.html", content)


def idea_add(request):  # добавление идеи через форму

    if request.method == 'POST':
        username = request.user.username

        title = request.POST['title']
        rubrics = request.POST['rubrics']
        preview = request.POST['preview']
        body = request.POST['body']
        if title and rubrics and preview and body:  # проверка наличия данных во всех полях

            new_idea = Idea.objects.create(autor=username, title=title, rubrics=rubrics,
                                           preview=preview, body=body)
            new_idea.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def idea_edit(request, pk):  # изменение идеи через форму

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


def idea_delete(request, pk):  # удаление идеи при нажатии на кнопку

    idea = Idea.objects.filter(pk=pk)
    idea.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" отзывы. добавление, удаление, изменение """


def feedback_add(request, pk):  # добавление отзыва через форму

    if request.method == 'POST':
        idea = Idea.objects.filter(pk=pk).first()

        try:
            rating = request.POST['rating']
        except:
            rating = 5
        feedback = request.POST['feedback_text']

        new_feedback = Feedback.objects.create(idea=idea, rating=rating, feedback=feedback)
        new_feedback.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def feedback_edit(request, pk):  # изменение отзыва через форму

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


def feedback_delete(request, pk):  # удаление отзыва при нажатии на кнопку

    feedback = Feedback.objects.filter(pk=pk)
    feedback.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" Другие пользователи могут присоединиться к идее и удалятся """


def joined_user_add(request, pk):  # добавление пользователя в проект через форму

    idea = Idea.objects.filter(pk=pk).first()
    autor = request.user.nickname

    new_joined_user = JoinedUsers.objects.create(idea=idea, autor=autor)
    new_joined_user.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def joined_user_delete(request, pk):  # удаление пользователя из проекта при нажатии на кнопку

    idea = Feedback.objects.filter(pk=pk).first()
    autor = request.user.nickname

    joined_user = JoinedUsers.objects.filter(idea=idea, autor=autor).first()
    joined_user.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" Другие пользователи могут поставить лпйк к идее """


def like_add(request, pk): # добавление лайка на проект через кнопку

    idea = Idea.objects.filter(pk=pk).first()
    autor = request.user.nickname

    new_like = LikesToIdeas.objects.create(idea=idea, autor=autor)
    new_like.save()
    print(new_like)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def like_delete(request, pk): # удаление лайка на проект через кнопку

    idea = Feedback.objects.filter(pk=pk).first()
    autor = request.user.nickname

    like = LikesToIdeas.objects.filter(idea=idea, autor=autor).first()
    like.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

