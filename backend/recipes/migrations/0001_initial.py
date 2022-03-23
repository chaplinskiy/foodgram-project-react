# Generated by Django 2.2.16 on 2022-03-23 01:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название ингредиента')),
                ('measurement_unit', models.CharField(max_length=200, verbose_name='Единицы измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999, 'Не более 999'), django.core.validators.MinValueValidator(1, 'Не менее 1')], verbose_name='Время приготовления (в минутах)')),
                ('image', models.ImageField(blank=True, upload_to='recipes/images', verbose_name='Картинка')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredientAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Количество/ингредиент',
                'verbose_name_plural': 'Количества/ингредиент',
            },
        ),
        migrations.CreateModel(
            name='RecipeTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Тег/рецепт',
                'verbose_name_plural': 'Теги/рецепт',
            },
        ),
        migrations.CreateModel(
            name='RecipeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Избранное/рецепт',
                'verbose_name_plural': 'Избранные/рецепт',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название тега')),
                ('color', models.CharField(max_length=7, null=True, verbose_name='Цвет')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='RecipeUserCart',
            fields=[
                ('recipeuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recipes.RecipeUser')),
            ],
            options={
                'verbose_name': 'Список покупок/рецепт',
                'verbose_name_plural': 'Списки покупок/рецепт',
                'ordering': ['-id'],
            },
            bases=('recipes.recipeuser',),
        ),
    ]
