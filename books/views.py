from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookReviewForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Book, Book_Review, Author, Book_Author
from django.views import View
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.


class BookView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q')
        if search_query:
            books = Book.objects.filter(title__icontains=search_query)
        page_size = request.GET.get('page_size', 20)
        paginator = Paginator(books, page_size)
        page_num = request.GET.get('page', 1)
        page = paginator.get_page(page_num)
        return render(request, 'books/list.html', {
            'books': books,
            'page': page
        })


class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        form = BookReviewForm()
        return render(request, 'books/detail.html', {
            'book': book,
            'form': form,
        })

    def post(self, request, id):
        pass


class BookReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        print(book.title)
        form = BookReviewForm(request.POST)
        if form.is_valid():
            Book_Review.objects.create(
                book=book,
                user=request.user,
                star_given=form.cleaned_data.get('star_given'),
                comment=form.cleaned_data.get('comment')
            )
            return redirect(reverse('detail', kwargs={
                'id': book.id
            }))
        return render(request, 'books/detail.html', {
            'book': book,
            'form': form,
        })


class AuthorView(View):
    def get(self,request,id):
        author=Author.objects.get(id=id)
        books=Book_Author.objects.filter(author=author)
        return render(request,'books/author.html',{
            'author':author
        })