from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.BookList.as_view(), name='home'),
    path('home/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('home/create/', views.CreateBook.as_view(), name='add_book'),
    path('home/<int:pk>/create/', views.EditBook.as_view(), name='edit_book'),
    path('home/<int:pk>/delete/', views.DeleteBook.as_view(), name='delete_book'),
]
