# Generated by Django 2.2.16 on 2022-01-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_auto_20220126_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(through='recipes.RecipeTag', to='recipes.Tag', verbose_name='Теги'),
        ),
    ]
