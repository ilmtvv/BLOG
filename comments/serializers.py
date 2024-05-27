from rest_framework import serializers

from comments.models import Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    author: serializers.PrimaryKeyRelatedField = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created_at', 'updated_at']
