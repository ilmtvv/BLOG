from datetime import datetime

from django.core.exceptions import ValidationError


def validate_password(value: str) -> str:
    if len(value) < 8 or not any(char.isdigit() for char in value):
        raise ValidationError('Password must be at least 8 characters long and include numbers.')
    return value


def validate_email(value: str) -> str:
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f'Email domain must be one of the following: {", ".join(allowed_domains)}')
    return value


def validate_birth_date(value: str) -> str:
    try:
        value.strftime('%Y-%m-%d')
    except ValueError:
        raise ValidationError('Birth date must be in the format YYYY-MM-DD')
    return value
