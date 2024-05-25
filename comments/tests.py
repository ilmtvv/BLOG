from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from comments.models import Comment
from posts.models import Post
from users.models import User


class CommentTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='test@mail.ru',
            phone='1234567890',
            birth_date='2000-01-01'  # Формат YYYY-MM-DD для модели
        )
        self.post = Post.objects.create(
            title='Test Post',
            text='This is a test post',
            author=self.user
        )
        self.comment_data = {
            'author': self.user.id,
            'post': self.post.id,
            'text': 'This is a test comment'
        }
        self.comment = Comment.objects.create(**self.comment_data)

        # Авторизация пользователя
        self.token = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpassword123'
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_comment(self) -> None:
        response = self.client.post(reverse('comment-list'), self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], self.comment_data['text'])

    def test_read_comment(self) -> None:
        response = self.client.get(reverse('comment-detail', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.comment_data['text'])

    def test_update_comment(self) -> None:
        new_comment_data = {'text': 'This is an updated test comment'}
        response = self.client.patch(reverse('comment-detail', kwargs={'pk': self.comment.pk}), new_comment_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], new_comment_data['text'])

    def test_delete_comment(self) -> None:
        response = self.client.delete(reverse('comment-detail', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_unauthorized_comment_creation(self) -> None:
        self.client.credentials()  # Сброс авторизации
        response = self.client.post(reverse('comment-list'), self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
