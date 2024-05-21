from django.core.management import BaseCommand
from dotenv import load_dotenv

from config.settings import BASE_DIR


class Command(BaseCommand):
    """Выгрузка переменных окружения из .env"""
    def handle(self, *args, **options) -> None:
        load_dotenv(BASE_DIR / '.env')
