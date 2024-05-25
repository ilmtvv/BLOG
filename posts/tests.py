from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from posts.models import Post
from users.models import User


class PostTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword123', email='test@mail.ru', phone='1234567890', birth_date='2000-01-01')
        self.post_data = {
            'title': 'Test Post',
            'text': 'This is a test post.',
            'author': self.user.id
        }
        self.post = Post.objects.create(**self.post_data)

    def test_create_post(self) -> None:
        token = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user.username,
            'password': 'testpassword123'
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(reverse('post-list'), self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_post(self) -> None:
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self) -> None:
        token = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user.username,
            'password': 'testpassword123'
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.patch(reverse('post-detail', kwargs={'pk': self.post.pk}), {'text': 'Updated text.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Updated text.')

    def test_delete_post(self) -> None:
        token = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user.username,
            'password': 'testpassword123'
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
