# Generated by Django 3.2.16 on 2023-03-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0004_alter_shopuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
        ),
    ]
