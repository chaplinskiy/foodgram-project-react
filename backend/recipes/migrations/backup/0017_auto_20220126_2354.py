# Generated by Django 2.2.16 on 2022-01-26 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_auto_20220126_2229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeIngredient',
            new_name='RecipeIngredientAmount',
        ),
    ]