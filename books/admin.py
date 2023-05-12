from django.contrib import admin
from .models import Book,Author,Book_Author,Book_Review

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','isbn']
    search_fields = ['title','isbn']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    search_fields = ['email','last_name']

@admin.register(Book_Author)
class Book_AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_Review)
class Book_ReviewAdmin(admin.ModelAdmin):
    list_display = ['star_given','comment']
    search_fields = ['star_given',]