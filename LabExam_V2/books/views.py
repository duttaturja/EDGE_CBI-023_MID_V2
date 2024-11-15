from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from books.models import Book, Author
# Create your views here.

class BookListView(ListView):
    model = Book    
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        author_id = 1
        books = Book.objects.filter(author_id= author_id)
        return books
    
