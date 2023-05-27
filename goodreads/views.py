from django.shortcuts import render
from books.models import Book_Review
from django.core.paginator import Paginator


def home(request):
    reviews = Book_Review.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 20)
    paginator = Paginator(reviews, page_size)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'goodreads/index.html', {
        'reviews': page_obj
    })
