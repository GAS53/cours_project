from django.db import models

import uuid

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from authapp.models import BaseIdeinerUser


# Базовые абстрактные менеджер и таблица

class AbstractManager(models.Manager):
    '''абстрактный менеджер для передачи по api'''
    def get_object_by_public_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def get_queryset(self):
        return super().get_queryset().all()


""" Дата создания/изменения/удаления"""
class AbstractManager(models.Manager):
    def get_object_by_public_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

class DataTimeModel(models.Model):
    objects = AbstractManager()
    id = models.UUIDField(db_index=True, primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=False)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, editable=False)
    deleted = models.BooleanField(verbose_name='Запись удалена', default=False)


    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ('-created',)  # '-' говорит об обратной сортировке
        abstract = True  # важный флаг для исключения дублирования




class Rubric(DataTimeModel):
    rubirc_name = models.CharField(verbose_name='Название рубрики', max_length=36)
    
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


    def __str__(self):
        return f'{self.rubirc_name}'


class Idea(DataTimeModel):
    autor = models.ForeignKey(BaseIdeinerUser, on_delete=models.CASCADE)
    rubric = models.ForeignKey(Rubric, on_delete=models.DO_NOTHING)

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    preview = models.CharField(verbose_name='Описание', max_length=1000)
    body = models.TextField(verbose_name='Содержание')

    def __str__(self) -> str:
        return f'{self.autor} {self.title} {self.rubric}'


class Meta:
    verbose_name = 'Идея'
    verbose_name_plural = 'Идеи'
    ordering = DataTimeModel.Meta.ordering


''' Отзывы '''


class Feedback(DataTimeModel):
    RATING_FIVE = 5

    RATINGS = (
        (RATING_FIVE, '⭐⭐⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (3, '⭐⭐⭐'),
        (2, '⭐⭐'),
        (1, '⭐'),
    )
    
    idea = models.ForeignKey(Idea, verbose_name='Идея', on_delete=models.CASCADE, related_name='feedback')
    liker = models.ManyToManyField(BaseIdeinerUser)
    rating = models.SmallIntegerField(verbose_name='Рейтинг', choices=RATINGS, default=RATING_FIVE)
    feedback = models.TextField(verbose_name='Отзыв', default='Без отзыва')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self) -> str:
        return f'Отзыв на {self.idea.title} от {self.idea.autor}'


""" присоеденённые к проектам пользователи """


class JoinedUser(DataTimeModel):
    idea = models.ForeignKey(Idea, verbose_name='Идея', on_delete=models.CASCADE, related_name='joinedUser')
    user = models.ManyToManyField(BaseIdeinerUser)

    def __str__(self) -> str:
        return f'{self.user} присоединился к {self.idea.title}'


class LikesToIdea(DataTimeModel):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, verbose_name='Идея', related_name='likesToIdea')
    autor = models.ForeignKey(BaseIdeinerUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.autor} поставил лайк на {self.idea.title}'
