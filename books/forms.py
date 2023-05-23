from django import forms
from .models import Book_Review


class BookReviewForm(forms.ModelForm):
    star_given = forms.IntegerField(required=True, min_value=1, max_value=5)

    class Meta:
        model = Book_Review
        fields = ['comment', 'star_given']
