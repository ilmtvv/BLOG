
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from users.models import User


class UserTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'test@mail.ru',
            'phone': '1234567890',
            'birth_date': '01-01-2000'  # Формат DD-MM-YYYY
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_user(self) -> None:
        response = self.client.post(reverse('user-list'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_jwt_auth(self) -> None:
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_read_user(self) -> None:
        token = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self) -> None:
        token = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.patch(reverse('user-detail', kwargs={'pk': self.user.pk}), {'phone': '0987654321'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone'], '0987654321')

    def test_delete_user(self) -> None:
        token = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }).data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
