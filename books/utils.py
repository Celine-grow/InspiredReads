import requests
from django.conf import settings

def get_books_by_genre(genre_name):
    api_key = settings.GOOGLE_BOOKS_API_KEY
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=subject:{genre_name}&key={api_key}')
    if response.status_code == 200:
        books = response.json().get('items', [])
        return books
    else:
        return []
