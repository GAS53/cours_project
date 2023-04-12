from django.core.management import BaseCommand

from authapp.models import BaseIdeinerUser
from backend.models import Rubric, Idea, LikesToIdea


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаем пользователей
        users = []
        for i in range(1, 4):
            if not BaseIdeinerUser.objects.filter(email=f'test{i}@test.com'):
                BaseIdeinerUser.objects.create_user(login=f'login{i}',
                                                    email=f'test{i}@test.com',
                                                    first_name=f'name{i}',
                                                    last_name=f'name{i}',
                                                    password='1234')
            users.append(BaseIdeinerUser.objects.filter(email=f'test{i}@test.com').first())

        # Создаем рубрики
        RUBRIC_PYTHON = 'Python'
        RUBRIC_JAVASCRIPT = 'JavaScript'
        rubrics = (RUBRIC_PYTHON, RUBRIC_JAVASCRIPT)
        for rubric in rubrics:
            if not Rubric.objects.filter(rubirc_name=rubric).first():
                Rubric.objects.create(rubirc_name=rubric)

        # Создаем идеи
        rubric_python = Rubric.objects.filter(rubirc_name=RUBRIC_PYTHON).first()
        rubric_javascript = Rubric.objects.filter(rubirc_name=RUBRIC_JAVASCRIPT).first()

        if not Idea.objects.filter(title=f'Заголовок идеи 1').first():
            Idea.objects.create(autor=users[1], title=f'Заголовок идеи 1', rubric=rubric_javascript,
                                       preview=f'Описание идеи 1', body=f'Содержание идеи 1')
        idea = Idea.objects.filter(title=f'Заголовок идеи 1').first()

        for i in range(2, 4):
            if not Idea.objects.filter(title=f'Заголовок идеи {i}'):
                Idea.objects.create(autor=users[1], title=f'Заголовок идеи {i}', rubric=rubric_python,
                                    preview=f'Описание идеи {i}', body=f'Содержание идеи {i}')

        # Создаем лайки идеи
        if not LikesToIdea.objects.filter(idea=idea, autor=users[1]).first():
            LikesToIdea.objects.create(idea=idea, autor=users[1])
        if not LikesToIdea.objects.filter(idea=idea, autor=users[2]).first():
            LikesToIdea.objects.create(idea=idea, autor=users[2])
