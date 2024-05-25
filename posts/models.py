from django.db import models

from users.models import User


class Post(models.Model):
    title: str = models.CharField(max_length=255)
    text: str = models.TextField()
    image: models.ImageField = models.ImageField(upload_to='posts/', null=True, blank=True)
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
