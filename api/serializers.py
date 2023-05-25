from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    desc=serializers.CharField()
    isbn=serializers.CharField(max_length=17)


class UserSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)


class BookReviewSerializer(serializers.Serializer):
    star_given=serializers.IntegerField(min_value=1,max_value=5)
    comment=serializers.CharField()
    book=BookSerializer(read_only=True)
    user=UserSerializer(read_only=True)
    book_id=serializers.IntegerField(write_only=True)
    user_id=serializers.IntegerField(write_only=True)