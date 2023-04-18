from django.urls import reverse
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render
from .models import Idea, Feedback, Rubric
from authapp.models import BaseIdeinerUser
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import IsAuthenticated, BasePermission

from backend.models import JoinedUser
class Temp(TemplateView):
    template_name = 'backend/index.html'


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff





def GenIdeasList(ideas, user=None):
    
    # генератор списка идей.
    # создаёт словарь, в котором ключ это порядковое число, а значение это словарь с отзывами и идеями
    # возвращает словарь со со всеми отзывами и идями
    # в html прогоняется циклом for item in ideas.values
    # в нём идеи вызываются так: item.idea, а отызывы так: item.feedback

    sl_ideas = {}
    a = 0
    likes_user_pk = []
    joines_user_pk = []
    if user and user.is_authenticated:
        likes_user_pk = LikesToIdea.objects.filter(autor=user, deleted=False).values_list('idea', flat=True)
        joines_user_pk = JoinedUser.objects.filter(user=user, deleted=False).values_list('idea', flat=True)
    for idea in ideas:
        liked = False
        joined = False
        if idea.pk in likes_user_pk:
            liked = True
        if idea.pk in joines_user_pk:
            joined = True

        a += 1
        sl_ideas[a] = {"feedback": Feedback.objects.filter(idea=idea),
                       "liked": liked, "joined": joined, "idea": idea}

    return sl_ideas


""" Личный кабинет """

def lk(request):  # профиль

    title = "Профиль"

    content = {"title": title, "media_url": settings.MEDIA_URL}

    return render(request, "backend/lk.html", content)


def lk_edit(request):  # изменение профиля через форму

    if request.method == 'POST':
        user = BaseIdeinerUser.objects.filter(id=request.user.id).first()
        print(request.POST)

        if request.POST['first_name']: user.first_name = request.POST['first_name']
        if request.POST['last_name']: user.last_name = request.POST['last_name']
        if request.POST['email']: user.email = request.POST['email']
        if request.POST['age']: user.age = request.POST['age']

        user.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" главная """


def main(request):  # список всех идей.
    title = "Идеи"

    ideas = GenIdeasList(Idea.objects.all(), request.user)

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "backend/index.html", content)
 


""" админка """

@user_passes_test(lambda u: u.is_superuser)
def admin(request):
    title = "Админка"
    
    ideas = GenIdeasList(Idea.objects.all())

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "backend/admin.html", content)


""" поисковик """


def search(request):
    if request.method == 'POST':

        title = "Поиск"
        name = request.POST['search']

        ideas = Idea.objects.all()
        ideas_list = []
        for idea in ideas:
            if name in idea.title:
                ideas_list.append(idea)

        ideas_sl = GenIdeasList(ideas_list)

        content = {"title": title, "ideas": ideas_sl, "media_url": settings.MEDIA_URL}

        return render(request, "backend/index.html", content)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" идеи """

@user_passes_test(lambda u: u.is_authenticated)
def my_ideas(request):
    title = "Мои идели"

    ideas = GenIdeasList(Idea.objects.filter(autor=request.user))

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "backend/my_ideas.html", content)



def idea_add(request):  # добавление идеи через форму

    if request.method == 'POST':
        title = request.POST['title']
        preview = request.POST['preview']
        body = request.POST['body']

        try:
            rubrics = request.POST['rubrics']
        except:
            rubrics = "Python"

        # Затычка. Находит рубрику по названию или создает
        rubric = Rubric.objects.filter(rubirc_name=rubrics).first()
        if not rubric:
            rubric = Rubric.objects.create(rubirc_name=rubrics)

        if title and rubrics and preview and body:  # проверка наличия данных во всех полях

            new_idea = Idea.objects.create(autor=request.user, title=title, rubric=rubric,
                                           preview=preview, body=body)
            new_idea.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def idea_card(request, pk): # карта идеи
    title = "Идея"
    idea = Idea.objects.filter(pk=pk).first()
    feedbacks = Feedback.objects.filter(idea=idea)
    joined_users = JoinedUser.objects.filter(idea=idea)
    likes = LikesToIdea.objects.filter(idea=idea)
    if request.user and JoinedUser.objects.filter(idea=idea, user=request.user, deleted=False):
        i_joined = True
    else:
        i_joined = False

    rating_sum = 0
    for feedback in feedbacks:
        rating_sum += feedback.rating
    rating = round(rating_sum / len(feedbacks))*'⭐'


    content = {"title": title, "idea": idea, "feedbacks": feedbacks, "joined_users": joined_users, 
               "likes": likes, "i_joined": i_joined, 'rating': rating ,
               "media_url": settings.MEDIA_URL}

    return render(request, "backend/idea_card.html", content)


def idea_card_delete(request, pk):  # удаление идеи при нажатии на кнопку

    title = "Идеи"

    idea = Idea.objects.filter(pk=pk)
    idea.delete()

    ideas = GenIdeasList(Idea.objects.all())

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}
    return render(request, "backend/index.html", content)


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
    # autor = request.user.last_name
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('authapp:login'))

    # if JoinedUser.objects.filter(idea=idea, user=request.user):
    #     return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    new_joined_user = JoinedUser.objects.filter(idea=idea, user=request.user).first()
    if not new_joined_user:
        new_joined_user = JoinedUser.objects.create(idea=idea, user=request.user)
    new_joined_user.deleted = False
    new_joined_user.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def joined_user_delete(request, pk):  # удаление пользователя из проекта при нажатии на кнопку

    idea = Idea.objects.filter(pk=pk).first()

    joined_user = JoinedUser.objects.filter(idea=idea, user=request.user).first()
    joined_user.delete()
    joined_user.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" Другие пользователи могут поставить лпйк к идее """
from backend.models import LikesToIdea

def like_add(request, pk): # добавление лайка на проект через кнопку

    idea = Idea.objects.filter(pk=pk).first()
    # autor = request.user.login
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('authapp:login'))

    new_like = LikesToIdea.objects.filter(idea=idea, autor=request.user).first()
    if not new_like:
        new_like = LikesToIdea.objects.create(idea=idea, autor=request.user)
    new_like.deleted = False
    new_like.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def like_delete(request, pk): # удаление лайка на проект через кнопку

    idea = Idea.objects.filter(pk=pk).first()
    # autor = request.user.nickname

    like = LikesToIdea.objects.filter(idea=idea, autor=request.user).first()
    like.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

