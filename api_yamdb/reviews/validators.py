from django.core.validators import ValidationError
from django.utils import timezone


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            (f'Год {value} больше текущнго года!')
        )
