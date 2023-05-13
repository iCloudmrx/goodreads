from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views import View

# Create your views here.


class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/list.html', {
            'books': books
        })


class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        return render(request, 'books/detail.html', {
            'book': book
        })

    def post(self, request, id):
        pass
