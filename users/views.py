from typing import Any

from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission

from users.models import User
from users.permissions import IsAdminOrSelf as UserIsAdminOrSelf
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset: Any = User.objects.all()
    serializer_class: Any = UserSerializer

    def get_permissions(self, ) -> list[BasePermission]:
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [UserIsAdminOrSelf]
        elif self.action == 'list':
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
