from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.


class BookTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(reverse('list'))
        self.assertContains(response, 'No books found.')

    def test_book_list(self):
        Book.objects.create(title='test1', desc='description1', isbn=123456789)
        Book.objects.create(title='test2', desc='description2', isbn=123458524)
        Book.objects.create(title='test3', desc='description3', isbn=123458752)

        response = self.client.get(reverse('list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_book_detail(self):
        book = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        response = self.client.get(reverse('detail',
                                           kwargs={
                                               'id': book.id
                                           }))
        self.assertContains(response, book.title)
        self.assertContains(response, book.desc)
