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
    username = models.CharField(max_length=100, unique=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    ),
    role = EnumChoiceField(RoleChoice, default=RoleChoice.USER),
    email = models.EmailField(max_length=100, unique=True)


    def __str__(self):
        return self.name
    

def generate_confirmation_code():
    return random.randint(1000, 9999)


class ConfirmationCode(models.Model):
    code = models.IntegerField(),
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
