from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from books.models import Book,Book_Review
from rest_framework.reverse import reverse

# Create your tests here.
class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.db_user=User.objects.create(username="test",
                                         first_name="test")
        self.db_user.set_password('test123')
        self.db_user.save()

    def test_book_review_detail(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        review= Book_Review.objects.create(
            book=book1,
            user=self.db_user,
            star_given=5,
            comment='Very good book'
        )
        response=self.client.get(reverse('detail',kwargs={'id': review.id}))

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['star_given'], review.star_given)
        self.assertEqual(response.data['comment'], review.comment)
        self.assertEqual(response.data['book']['title'], review.book.title)
        self.assertEqual(response.data['book']['desc'], review.book.desc)
        self.assertEqual(response.data['user']['username'], review.user.username)
        self.assertEqual(response.data['user']['first_name'], review.user.first_name)

    def test_delete_review(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        review = Book_Review.objects.create(
            book=book1,
            user=self.db_user,
            star_given=5,
            comment='Very good book'
        )
        response = self.client.delete(reverse('detail', kwargs={'id': review.id}))

        self.assertEqual(response.status_code,204)
        self.assertFalse(Book_Review.objects.filter(id=book1.id).exists())

    def test_patch_review(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        review = Book_Review.objects.create(
            book=book1,
            user=self.db_user,
            star_given=5,
            comment='Very good book'
        )
        response = self.client.patch(reverse('detail', kwargs={'id': review.id}),data={
            'star_given':4
        })
        review.refresh_from_db()
        self.assertEqual(response.status_code,200)
        self.assertEqual(review.star_given,4)

    def test_put_review(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        review = Book_Review.objects.create(
            book=book1,
            user=self.db_user,
            star_given=5,
            comment='Very good book'
        )
        response = self.client.put(reverse('detail',
                                             kwargs={'id': review.id}),
                                     data={
                                        'star_given':4,
                                         'comment':'menga yoqdi',
                                         'user_id':self.db_user.id,
                                         'book_id':book1.id
                                        })
        review.refresh_from_db()

        self.assertEqual(response.status_code,200)
        self.assertEqual(review.star_given,4)

    def test_create_review(self):
        book1 = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        response = self.client.post(reverse('detail'),
                                     data={
                                        'star_given':4,
                                         'comment':'menga yoqdi',
                                         'user_id':self.db_user.id,
                                         'book_id':book1.id
                                        })

        self.assertEqual(response.status_code,201)

        review=Book_Review.objects.get(book=book1)

        self.assertEqual(review.star_given,4)
        self.assertEqual(review.comment,'menga yoqdi')

    def test_book_review_list(self):
        book = Book.objects.create(
            title='test1', desc='description1', isbn=123456789)
        user = User.objects.create(username="test2",
                                           first_name="test2")
        user.set_password('test123')
        user.save()
        book2 = Book.objects.create(
            title='test2', desc='description2', isbn=1234568554)
        review = Book_Review.objects.create(
            book=book,
            user=self.db_user,
            star_given=5,
            comment='Very good book'
        )
        review2 = Book_Review.objects.create(
            book=book2,
            user=user,
            star_given=5,
            comment='Very bad book'
        )
        response=self.client.get(reverse('list'))


        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),2)


        self.assertEqual(response[0]['star_given'], 5)
        self.assertEqual(response[0]['comment'], review2.comment)

        self.assertEqual(response[1]['star_given'], 5)
        self.assertEqual(response[1]['comment'], review.comment)
