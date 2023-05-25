from django.test import TestCase
from books.models import Book, Book_Review
from django.contrib.auth.models import User
from django.urls import reverse


class HomeViewTestCase(TestCase):
    def test_paginated_list(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        user = User.objects.create(
            username='test',
            first_name='test',
            last_name='test',
            email='test@gmail.com')
        user.set_password('test')
        user.save()
        review1 = Book_Review(user=user, book=book1,
                              star_given=4, comment="Very best1")
        review2 = Book_Review(user=user, book=book1,
                              star_given=2, comment="Very bes2")
        review3 = Book_Review(user=user, book=book1,
                              star_given=3, comment="Very best3")

        response = self.client.get(reverse('home')+'?page_size=2')

        self.assertContains(response, review2.star_given)
        self.assertContains(response, review3.star_given)
