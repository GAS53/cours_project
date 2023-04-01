from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render
from .models import Idea, Feedback, JoinedUsers, LikesToIdeas
from authapp.models import BaseIdeinerUser
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import IsAuthenticated, BasePermission

class Temp(TemplateView):
    template_name = 'backend/index.html'


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff





def GenIdeasList(ideas):
    
    # генератор списка идей.
    # создаёт словарь, в котором ключ это порядковое число, а значение это словарь с отзывами и идеями
    # возвращает словарь со со всеми отзывами и идями
    # в html прогоняется циклом for item in ideas.values
    # в нём идеи вызываются так: item.idea, а отызывы так: item.feedback

    sl_ideas = {}
    a = 0
    for idea in ideas:
        a += 1
        sl_ideas[a] = {"feedback": Feedback.objects.filter(idea=idea), "idea": idea}

    return sl_ideas


""" Личный кабинет """

def lk(request):  # профиль

    title = "Профиль"

    content = {"title": title, "media_url": settings.MEDIA_URL}

    return render(request, "backend/lk.html", content)


def lk_edit(request):  # изменение профиля через форму

    if request.method == 'POST':

        nickname = request.user.nickname
        user = BaseIdeinerUser.objects.filter(nickname=nickname).first()

        if request.POST['nickname']: user.nickname = request.POST['nickname']
        if request.POST['username']: user.username = request.POST['username']
        if request.POST['surname']: user.surname = request.POST['surname']
        if request.POST['email']: user.email = request.POST['email']
        if request.POST['age']: user.age = request.POST['age']

        user.save()

        print(request.POST['nickname'], request.user.nickname, bool(request.POST['nickname']))

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" главная """


def main(request):  # список всех идей.
    title = "Идеи"

    ideas = GenIdeasList(Idea.objects.all())

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
    autor = request.user.username

    ideas = GenIdeasList(Idea.objects.filter(autor=autor))

    content = {"title": title, "ideas": ideas, "media_url": settings.MEDIA_URL}

    return render(request, "backend/my_ideas.html", content)



def idea_add(request):  # добавление идеи через форму

    if request.method == 'POST':
        username = request.user.username

        title = request.POST['title']
        preview = request.POST['preview']
        body = request.POST['body']

        try:
            rubrics = request.POST['rubrics']
        except:
            rubrics = "Python"

        if title and rubrics and preview and body:  # проверка наличия данных во всех полях

            new_idea = Idea.objects.create(autor=username, title=title, rubrics=rubrics,
                                           preview=preview, body=body)
            new_idea.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def idea_card(request, pk): # карта идеи
    title = "Идея"
    idea = Idea.objects.filter(pk=pk).first()
    feedbacks = Feedback.objects.filter(idea=idea)
    joined_users = JoinedUsers.objects.filter(idea=idea)
    likes = LikesToIdeas.objects.filter(idea=idea)
    print(pk, idea, Idea.objects.all())

    content = {"title": title, "idea": idea, "feedbacks": feedbacks, "joined_users": joined_users, 
               "likes": likes, "media_url": settings.MEDIA_URL}

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
    autor = request.user.nickname

    new_joined_user = JoinedUsers.objects.create(idea=idea, autor=autor)
    new_joined_user.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def joined_user_delete(request, pk):  # удаление пользователя из проекта при нажатии на кнопку

    idea = Feedback.objects.filter(pk=pk).first()
    autor = request.user.username

    joined_user = JoinedUsers.objects.filter(idea=idea, autor=autor).first()
    joined_user.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


""" Другие пользователи могут поставить лпйк к идее """


def like_add(request, pk): # добавление лайка на проект через кнопку

    idea = Idea.objects.filter(pk=pk).first()
    autor = request.user.username

    new_like = LikesToIdeas.objects.create(idea=idea, autor=autor)
    new_like.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def like_delete(request, pk): # удаление лайка на проект через кнопку

    idea = Feedback.objects.filter(pk=pk).first()
    autor = request.user.nickname

    like = LikesToIdeas.objects.filter(idea=idea, autor=autor).first()
    like.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

