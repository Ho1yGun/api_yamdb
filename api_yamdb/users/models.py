from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    # Константы заглавными буквами ROLE_CHOISES.
    # Название выбора в константы.
    ROLE_CHOISES = {
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    }
    bio = models.TextField(
        'Краткая информация',
        blank=True,
        null=True
    )
    role = models.CharField(
        'Роль',
        max_length=50,
        choices=ROLE_CHOISES,
        default=USER
    )

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff

    def __str__(self):
        # Такого поля нет у User.
        # return self.name
        return self.username


def generate_confirmation_code():
    return random.randint(1000, 9999)


class ConfirmationCode(models.Model):
    code = models.IntegerField(),
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
