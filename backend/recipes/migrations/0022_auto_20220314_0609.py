# Generated by Django 2.2.16 on 2022-03-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0021_auto_20220314_0609'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='recipeuser',
            name='unique_recipeusercart',
        ),
        migrations.AddConstraint(
            model_name='recipeuser',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_recipeuser'),
        ),
    ]
