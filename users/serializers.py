from typing import Dict, Any

from rest_framework import serializers

from users.models import User
from users.validators import validate_email, validate_password, validate_birth_date


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(validators=[validate_email])
    birth_date = serializers.DateField(format="%d-%m-%Y", input_formats=["%d-%m-%Y"], validators=[validate_birth_date])

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'birth_date', 'created_at', 'updated_at']

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User.objects.create_user(**validated_data)
        return user
