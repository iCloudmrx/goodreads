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
    def setUp(self):
        self.user = User.objects.create(
            username='test',
            first_name='test'
        )
        self.user.set_password('test')
        self.user.save()

    def test_successful_login(self):

        self.client.post(
            reverse('users:login'),
            data={
                'username': 'test',
                'password': 'test'
            }
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_logout(self):

        self.client.login(username='test', password='test')

        self.client.get(reverse('users:logout'))

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.url, '/users/login/?next=/users/profile/')

    def test_profile_detail(self):
        user = User.objects.create(
            username='test',
            first_name='test',
            last_name='test',
            email='test@gmail.com')
        user.set_password('test')
        user.save()

        self.client.login(username='test', password='test')

        response = self.client.get(reverse('users:profile'))

        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.username)
        self.assertContains(response, user.email)
        self.assertEqual(response.status_code, 200)
