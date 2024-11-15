from django.urls import path
from books.views import BookListView

urlpatterns = [
    path('list/', BookListView.as_view()),
]