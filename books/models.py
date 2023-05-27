from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.URLField(max_length=200)
    isbn = models.CharField(max_length=17)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    website= models.CharField(max_length=100,blank=True,null=True)
    born = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    member_since = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book_Author(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} by {self.author}"


class Book_Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)
    comment = models.TextField()
    star_given = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.star_given} by {self.user.username}"
