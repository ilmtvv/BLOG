from rest_framework import serializers

from posts.models import Post
from posts.validators import validate_title, validate_author_age
from users.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'author', 'created_at', 'updated_at']

    def validate(self, data):
        author = data.get('author')
        validate_author_age(author.birth_date.strftime('%d-%m-%Y'))
        return data
