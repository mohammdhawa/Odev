from django.shortcuts import render

# Create your views here.

from .models import Book

from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from .forms import SearchForm



class BookList(ListView):
    model = Book



class BookDetail(DetailView):
    model = Book



class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/home/'



class EditBook(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/home/'



class DeleteBook(DeleteView):
    model = Book
    success_url = '/home/'





def home2(request):
    items = Book.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        query = search_form.cleaned_data['search_query']
        items = items.filter(title__icontains=query)

    return render(request, 'book/book_list.html', {'book_list': items, 'form': search_form})