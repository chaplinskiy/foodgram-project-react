# Generated by Django 2.2.16 on 2022-02-01 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20220129_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999, 'Не более 999'), django.core.validators.MinValueValidator(1, 'Не менее 1')], verbose_name='Время приготовления (в минутах)'),
        ),
    ]
