from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create(
            username='admin',
            email='admin@yandex.ru',
            is_staff=True,
            is_superuser=True
        )
        admin.set_password('123qwe456rty')
        admin.user_pk = admin
        admin.save()
