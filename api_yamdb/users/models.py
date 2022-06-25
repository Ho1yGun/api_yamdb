from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
import enum
import random
from enumchoicefield import EnumChoiceField


class RoleChoice(enum.Enum):
    USER = 'user'
    MODERATOR = 'Moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    is_active = False
    bio = models.TextField(
        'Биография',
        blank=True,
    ),
    role = EnumChoiceField(RoleChoice, default=RoleChoice.USER),


    def __str__(self):
        return self.name
    

def generate_confirmation_code():
    return ''.join(random.randit(10000,9999))


class Confirm(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    confirmation_code = models.CharField(max_length = 4, default=generate_confirmation_code)
