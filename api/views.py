from django.shortcuts import render
from django.views import  View
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import BookReviewSerializer
from books.models import Book_Review


# Create your views here.
class BookReviewDetailAPI(APIView):
    def get(self,request,id):
        review=Book_Review.objects.get(id=id)
        serializer=BookReviewSerializer(review)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def delete(self, request,id):
        review = Book_Review.objects.get(id=id)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request,id):
        review=Book_Review.objects.get(id=id)
        serializer=BookReviewSerializer(instance=review,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,id):
        review = Book_Review.objects.get(id=id)
        serializer = BookReviewSerializer(instance=review, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookReviewListAPI(APIView):
    def get(self,request):
        reviews=Book_Review.objects.all()

        paginator=PageNumberPagination()
        page_obj=paginator.paginate_queryset(reviews,request)


        serializer=BookReviewSerializer(page_obj,many=True)
        return paginator.get_paginated_response(data=serializer.data)
    def post(self,request):
        serializer = BookReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)