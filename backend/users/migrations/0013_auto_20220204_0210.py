# Generated by Django 2.2.16 on 2022-02-04 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20220203_1254'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subscription',
            name='unique_list',
        ),
        migrations.RemoveConstraint(
            model_name='subscription',
            name='prevent_self_subscription',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='is_subscribed',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='subscription',
            name='followers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики пользователя'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Подписки пользователя'),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('following', 'followers'), name='unique_list'),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, following=django.db.models.expressions.F('followers')), name='prevent_self_subscription'),
        ),
    ]
