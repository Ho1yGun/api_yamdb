from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
import enum

from enumchoicefield import EnumChoiceField


class RoleChoice(enum.Enum):
    USER = 'user'
    MODERATOR = 'Moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    ),

    role = EnumChoiceField(RoleChoice, default=RoleChoice.USER)
