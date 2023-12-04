from django.test import TestCase
from .models import Book
from django.core.exceptions import ValidationError
from decimal import Decimal

class BookModelTest(TestCase):

    def test_book_creation(self):
        book = Book.objects.create(title="Test Book", pages=100, price=12.99)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.pages, 100)
        self.assertEqual(book.price, Decimal("12.99"))

    def test_empty_title_validation(self):
        with self.assertRaises(ValidationError):
            Book.objects.create(title="", pages=100, price=12.99)

    def test_invalid_pages_validation(self):
        with self.assertRaises(ValidationError):
            Book.objects.create(title="Test Book", pages="abc", price=12.99)

    def test_invalid_price_validation(self):
        with self.assertRaises(ValidationError):
            Book.objects.create(title="Test Book", pages=100, price="12.9a")

    def test_str_representation(self):
        book = Book.objects.create(title="Test Book", pages=100, price=12.99)
        self.assertEqual(str(book), "Test Book")
        

from django.test import TestCase
from .forms import SearchForm

class SearchFormTest(TestCase):

    def test_empty_query_validation(self):
        form = SearchForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["search_query"], ["This field is required."])

    def test_invalid_query_validation(self):
        form = SearchForm({"search_query": "1234"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["search_query"], ["Enter a valid search query."])

    def test_valid_query(self):
        form = SearchForm({"search_query": "book"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["search_query"], "book")


from django.test import TestCase, Client
from django.urls import reverse
from .models import Book

class BookListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.book1 = Book.objects.create(title="Book 1", pages=100, price=12.99)
        self.book2 = Book.objects.create(title="Book 2", pages=200, price=19.99)

    def test_renders_correct_template(self):
        response = self.client.get(reverse("home2"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book/book_list.html")

    def test_context_contains_all_books(self):
        response = self.client.get(reverse("home2"))
        self.assertEqual(len(response.context["book_list"]), 2)
        self.assertIn(self.book1, response.context["book_list"])
        self.assertIn(self.book2, response.context["book_list"])

    def test_search_functionality(self):
        response = self.client.get(reverse("home2"), {"search_query": "Book 2"})
        self.assertEqual(len(response.context["book_list"]), 1)
        self.assertEqual(response.context["book_list"][0], self.book2)

