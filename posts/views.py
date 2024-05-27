from django.shortcuts import render
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from users.permissions import IsAdminOrAuthor


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminOrAuthor]
        return super().get_permissions()
