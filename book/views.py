from django.shortcuts import render

# Create your views here.

from .models import Book

from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)



class BookList(ListView):
    model = Book



class BookDetail(DetailView):
    model = Book



class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/'



class EditBook(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/'



class DeleteBook(DeleteView):
    model = Book
    success_url = '/'
