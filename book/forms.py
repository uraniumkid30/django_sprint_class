from django import forms
from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(
        
        required=True,
        label="book title",
        help_text="give your book a unique name"
    )
    owner = forms.CharField()
    description = forms.CharField()
    rating = forms.IntegerField()


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "rating"]