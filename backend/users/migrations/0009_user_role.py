# Generated by Django 2.2.16 on 2022-01-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220127_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('guest', 'guest'), ('user', 'user'), ('admin', 'admin')], default='user', max_length=9, verbose_name='Уровень доступа'),
        ),
    ]
