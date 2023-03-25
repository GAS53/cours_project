from django.db import models
from django.conf import settings


""" Дата создания/изменения/удаления"""


class DataTimeModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Дата изменения',
                                      auto_now=True, editable=False)
    deleted = models.BooleanField(verbose_name='Запись удалена', default=False)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        # '-' говорит об обратной сортировке
        ordering = ('-created_at',)
        # важный флаг для исключения дублирования
        abstract = True


class ObjectsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().all()


class Idea(DataTimeModel):
    objects = ObjectsManager()
    autor = models.CharField(verbose_name='Никнейм', max_length=22)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    rubrics = models.CharField(verbose_name='Рубрика', max_length=255)  # тут надо подумать
    preview = models.CharField(verbose_name='Описание', max_length=1000)
    body = models.TextField(verbose_name='Содержание')

    body_as_markdown = models.BooleanField(verbose_name='Тип Идеи',  # тут не понял что это :(
                                           default=False)

    def __str__(self) -> str:
        return f'{self.autor} {self.title} {self.rubrics}'


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

    idea = models.ForeignKey(Idea, verbose_name='Идея', on_delete=models.CASCADE)
    rating = models.SmallIntegerField(verbose_name='Рейтинг', choices=RATINGS, default=RATING_FIVE)
    feedback = models.TextField(verbose_name='Отзыв', default='Без отзыва')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзовы'

    def __str__(self) -> str:
        return f'Отзыв на {self.idea.title} от {self.idea.autor}'


""" присоеденённые к проектам пользователи """


class JoinedUsers(DataTimeModel):
    idea = models.ForeignKey(Idea, verbose_name='Идея', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")

    def __str__(self) -> str:
        return f'{self.user.username} присоединился к {self.idea.idea.title}'


#class Rubrics()
