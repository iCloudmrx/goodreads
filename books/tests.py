from django.test import TestCase
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User
# Create your tests here.


class BookTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(reverse('list'))
        self.assertContains(response, 'No books found.')

    def test_book_list(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        book2 = Book.objects.create(
            title='test2', desc='description2', isbn=123458524)
        book3 = Book.objects.create(
            title='test3', desc='description3', isbn=123458752)

        response = self.client.get(reverse('list')+'?page=2')

        books = Book.objects.all()
        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('list')+'?page=2')

        self.assertContains(response, book3.title)

    def test_book_detail(self):
        book = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        response = self.client.get(reverse('detail',
                                           kwargs={
                                               'id': book.id
                                           }))
        self.assertContains(response, book.title)
        self.assertContains(response, book.desc)

    def test_search_book(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        book2 = Book.objects.create(
            title='test2', desc='description2', isbn=123458524)
        book3 = Book.objects.create(
            title='test3', desc='description3', isbn=123458752)

        response = self.client.get(reverse('list')+'?q=test')

        self.assertContains(response, book1.title)
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book3.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        user = User.objects.create(
            username='test',
            first_name='test',
            last_name='test',
            email='tugrp@example.com',
        )
        user.set_password('test')
        user.save()

        self.client.login(username='test', password='test')
        response = self.client.post(reverse('review', kwargs={
            'id': book.id
        }),
            data={
            'star_given': 5,
            'comment': 'Nice Book'
        })
        book_reviews = book.book_review_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].star_given, 5)
        self.assertEqual(book_reviews[0].comment, 'Nice Book')
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)
