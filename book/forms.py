# forms.py
import django_filters
from .models import Book
from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField()
    search_query = forms.CharField(max_length=255, required=False, label='Search')
