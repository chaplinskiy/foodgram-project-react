from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q


class UserRoles:
    GUEST = 'guest'
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (GUEST, GUEST),
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        verbose_name='Никнейм'
    )
    confirmation_code = models.CharField(
        max_length=100,
        editable=False,
        blank=True,
        null=True,
        unique=True,
        verbose_name='Код подтверждения'
    )
    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name='Электропочта'
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    role = models.CharField(
        max_length=9,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name='Уровень доступа'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.is_superuser or self.role == UserRoles.ADMIN

    def __str__(self):
        return self.username


class Subscription(models.Model):
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписки пользователя',
        null=True
    )
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчики пользователя',
        null=True
    )

    @property
    def email(self):
        return self.following.email

    @property
    def username(self):
        return self.following.username

    @property
    def first_name(self):
        return self.following.first_name

    @property
    def last_name(self):
        return self.following.last_name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['following', 'follower'],
                name='unique_subscription_list'
            ),
            models.CheckConstraint(
                check=~Q(following=F('follower')),
                name='prevent_self_subscription'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
