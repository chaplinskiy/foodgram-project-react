# Generated by Django 2.2.16 on 2022-01-25 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20220125_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'Количество/ингредиент', 'verbose_name_plural': 'Количества/ингредиент'},
        ),
        migrations.AlterModelOptions(
            name='recipetag',
            options={'verbose_name': 'Тег/рецепт', 'verbose_name_plural': 'Теги/рецепт'},
        ),
        migrations.AlterModelOptions(
            name='recipeuser',
            options={'verbose_name': 'Избранное/рецепт', 'verbose_name_plural': 'Избранные/рецепт'},
        ),
        migrations.AlterModelOptions(
            name='recipeusercart',
            options={'verbose_name': 'Списки покупок/рецепт'},
        ),
    ]
