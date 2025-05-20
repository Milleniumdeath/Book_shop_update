from django import forms
from .models import *
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=255)
    birth_year = forms.IntegerField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
