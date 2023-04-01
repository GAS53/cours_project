<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-03-29 14:07

from django.db import migrations, models
import django.db.models.deletion
import uuid
=======
# Generated by Django 4.1.7 on 2023-03-18 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> BW


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> BW
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
=======
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
>>>>>>> BW
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('autor', models.CharField(max_length=22, verbose_name='Никнейм')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('rubrics', models.CharField(max_length=255, verbose_name='Рубрика')),
                ('preview', models.CharField(max_length=1000, verbose_name='Описание')),
                ('body', models.TextField(verbose_name='Содержание')),
<<<<<<< HEAD
            ],
            options={
                'ordering': ('-created',),
=======
                ('body_as_markdown', models.BooleanField(default=False, verbose_name='Тип Идеи')),
            ],
            options={
                'ordering': ('-created_at',),
>>>>>>> BW
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikesToIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('autor', models.CharField(default='', max_length=22, verbose_name='Никнейм')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.idea', verbose_name='Идея')),
            ],
            options={
                'ordering': ('-created',),
=======
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.idea', verbose_name='Идея')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
>>>>>>> BW
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JoinedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('autor', models.CharField(default='', max_length=22, verbose_name='Никнейм')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.idea', verbose_name='Идея')),
            ],
            options={
                'ordering': ('-created',),
=======
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.idea', verbose_name='Идея')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
>>>>>>> BW
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
=======
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
>>>>>>> BW
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('rating', models.SmallIntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (2, '⭐⭐'), (1, '⭐')], default=5, verbose_name='Рейтинг')),
                ('feedback', models.TextField(default='Без отзыва', verbose_name='Отзыв')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.idea', verbose_name='Идея')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзовы',
            },
        ),
    ]
