from django.db import models

from posts.models import Post
from users.models import User


class Comment(models.Model):
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post: Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text: str = models.TextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
