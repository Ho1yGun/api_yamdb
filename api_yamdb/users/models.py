from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class Roles:
    USER = 'user'
    MODERATOR = 'Moderator'
    ADMIN = 'admin'
    # Константы заглавными буквами ROLE_CHOISES.
    # Название выбора в константы.
    ROLE_CHOISES = {
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    }

    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        'Имя',
        max_length=50,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        blank=True
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=150,
        unique=True
    )


#class User(AbstractUser):
#    Role_choises = [
#        ('user', Roles.USER),
#        ('moderator', Roles.MODERATOR),
#        ('admin', Roles.ADMIN)
#    ]
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
    #)
    #role = models.CharField(max_length=100, default = 'user', choices=Role_choises)
    #code = models.CharField(max_length=10)


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
    

def generate_confirmation_code():
    return random.randint(1000, 9999)


class ConfirmationCode(models.Model):
    code = models.IntegerField(default=1111)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')