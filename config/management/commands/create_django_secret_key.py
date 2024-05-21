from django.core.management import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    """Создание секретного ключа для django"""

    def handle(self, *args, **options) -> None:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        print(get_random_string(50, chars))
