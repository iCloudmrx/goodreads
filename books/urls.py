from django.urls import path
from .views import BookView, BookDetailView, BookReviewView,AuthorView

urlpatterns = [
    path('', BookView.as_view(), name='list'),
    path('<int:id>/detail/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/review/', BookReviewView.as_view(), name='review'),
    path('<int:id>/author/', AuthorView.as_view(), name='author'),

]
