from django.urls import path
from .views import BookReviewDetailAPI,BookReviewListAPI
urlpatterns=[
    path('reviews/',BookReviewListAPI.as_view(),name='list_api'),
    path('reviews/<int:id>/',BookReviewDetailAPI.as_view(),name='detail_api'),

]