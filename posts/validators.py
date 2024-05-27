import datetime

from django.core.exceptions import ValidationError
from django.utils import timezone

from users.models import User


def validate_author_age(author_birth_date: str) -> None:
    try:
        birth_date = datetime.datetime.strptime(author_birth_date, '%Y-%m-%d').date()
    except ValueError:
        raise ValidationError('Birth date must be in the format YYYY-MM-DD')

    if (datetime.date.today() - birth_date).days < 18 * 365:
        raise ValidationError('Author must be at least 18 years old.')


def validate_title(value: str) -> str:
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    if any(word in value.lower() for word in forbidden_words):
        raise ValidationError(f'Title cannot contain the words: {", ".join(forbidden_words)}')
    return value
