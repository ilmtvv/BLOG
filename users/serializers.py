from typing import Dict, Any

from rest_framework import serializers

from users.models import User
from users.validators import validate_email, validate_password


class UserSerializer(serializers.ModelSerializer):
    password: serializers.CharField = serializers.CharField(write_only=True, validators=[validate_password])
    email: serializers.EmailField = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'birth_date', 'created_at', 'updated_at']

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User.objects.create_user(**validated_data)
        return user
