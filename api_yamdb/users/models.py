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
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.name
    

def generate_confirmation_code():
    return random.randint(1000,9999)


class SignUp(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
