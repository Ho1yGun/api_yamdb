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

    roles = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLE_CHOISES,
        default=USER,
    )

    bio = models.TextField(
        'Биография',
        blank=True,
    ),

    # Код хранишь либо в User. Либо в модели ConfirmationCode.
    # Одно из двух выбери, второе выпили.
    code = models.CharField(max_length=10)

    def __str__(self):
        # Такого поля нет у User.
        # return self.name
        return self.username


def generate_confirmation_code():
    return random.randint(1000, 9999)


class ConfirmationCode(models.Model):
    code = models.IntegerField(),
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
