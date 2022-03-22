# Generated by Django 2.2.16 on 2022-02-04 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20220204_0210'),
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
            name='followers',
        ),
        migrations.AddField(
            model_name='subscription',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики пользователя'),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('following', 'follower'), name='unique_list'),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, following=django.db.models.expressions.F('follower')), name='prevent_self_subscription'),
        ),
    ]