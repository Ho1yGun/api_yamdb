from django.contrib.auth.models import AbstractUser
from django.db import models
import random
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class Roles:
    USER = 'user'
    MODERATOR = 'Moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    Role_choises = [
        ('user', Roles.USER),
        ('moderator', Roles.MODERATOR),
        ('admin', Roles.ADMIN)
    ]
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(max_length=100, default = 'user', choices=Role_choises)
    code = models.CharField(max_length=10,  blank=True, null= True)


    def __str__(self):
        return self.name
    
    @property
    def is_admin(self):
        return self.role == "admin" or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == "moderator"

    @property
    def is_user(self):
        return self.role == "user"

    def __str__(self):
        return f'{self.username}, статус: {self.role}'
    

generate_token = PasswordResetTokenGenerator()
