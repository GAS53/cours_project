from django.core.management import BaseCommand

from authapp.models import BaseIdeinerUser
from backend.models import Rubric


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаем пользователей
        for i in range(1, 4):
            if not BaseIdeinerUser.objects.filter(email=f'test{i}@test.com'):
                BaseIdeinerUser.objects.create_user(login=f'login{i}',
                                                    email=f'test{i}@test.com',
                                                    first_name=f'name{i}',
                                                    last_name=f'name{i}',
                                                    password='1234')

        # Создаем рубрики
        rubrics = ('Python', 'Javascript')
        for rubric in rubrics:
            if not Rubric.objects.filter(rubirc_name=rubric).first():
                Rubric.objects.create(rubirc_name=rubric)
