# Generated by Django 2.2.16 on 2022-02-03 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_role'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subscription',
            name='unique_list',
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('subscriber', 'is_subscribed')},
        ),
    ]
