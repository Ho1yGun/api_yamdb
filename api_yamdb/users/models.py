from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class Roles:
    USER = 'user'
    MODERATOR = 'Moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    is_active = False
    Role_choises = {
        ('user', Roles.USER),
        ('moderator', Roles.MODERATOR),
        ('admin', Roles.ADMIN)
    }
    bio = models.TextField(
        'Биография',
        blank=True,
    ),
    role = models.CharField(max_length=100, default = 'user', choices=Roles),
    code = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    

def generate_confirmation_code():
    return random.randint(1000, 9999)


class ConfirmationCode(models.Model):
    code = models.IntegerField(),
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
