from typing import Any

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

from comments.models import Comment
from comments.serializers import CommentSerializer
from users.permissions import IsAdminOrAuthor


class CommentViewSet(viewsets.ModelViewSet):
    queryset: Any = Comment.objects.all()
    serializer_class: Any = CommentSerializer

    def get_permissions(self) -> list[BasePermission]:
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminOrAuthor]
        return super().get_permissions()
    