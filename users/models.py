from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone: str = models.CharField(max_length=15)
    birth_date: models.DateField = models.DateField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
