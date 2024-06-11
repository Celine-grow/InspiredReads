from django.urls import path
from .views import recommended_books,select_genres,fetch_books_by_genre,fetch_books_page

app_name="books"
urlpatterns=[
    path('selected_genres/',select_genres,name="selected_genres"),
    path('recommended_books/',recommended_books,name='recommended_books'),
    path('fetch_booksPage/',fetch_books_page,name='fetch_books_page'),
    path('fetch_books/<str:genre_name>/',fetch_books_by_genre,name='fetch_books_by_genre'),
]