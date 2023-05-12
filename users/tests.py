from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user

# Create your tests here.


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                'username': 'test',
                'first_name': "test",
                "last_name": 'test',
                'email': 'tugrp@example.com',
                'password': 'test',

            }
        )
        user = User.objects.get(username='test')

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'test')
        self.assertNotEqual(user.password, 'test')
        self.assertEqual(user.email, 'tugrp@example.com')


class LoginTestCase(TestCase):
    def test_successful_login(self):
        user = User.objects.create(
            username='test',
            first_name='test'
        )
        user.set_password('test')
        user.save()

        self.client.post(
            reverse('users:login'),
            data={
                'username': 'test',
                'password': 'test'
            }
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
