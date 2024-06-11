from django.shortcuts import render,redirect
from .forms import  GenreSelectionForm
from .models import UserGenre,Genre
import requests
from .utils import get_books_by_genre
from  django.http import JsonResponse
from django.conf import settings
import logging
from django.contrib.auth.decorators import login_required

@login_required
def select_genres(request):
    if request.method == 'POST':
        form = GenreSelectionForm(request.POST)
        if form.is_valid():
            selected_genres = form.cleaned_data['genres']  # This should be a list of Genre objects
            print(selected_genres)  # Debug statement
            selected_genres_ids = [genre.id for genre in selected_genres]  # Convert to list of IDs
            user = request.user
            UserGenre.objects.filter(user=user).delete()
            for genre_id in selected_genres_ids:
                genre = Genre.objects.get(id=genre_id)
                UserGenre.objects.create(user=user, genre=genre)
            return redirect('books:recommended_books')
        else:
            # Handle invalid form
            pass
    else:
        form = GenreSelectionForm()
    return render(request, 'books/select_genre.html', {'form': form})


    
logger=logging.getLogger(__name__)

def fetch_books_by_genre(request,genre_name):
    api_key=settings.GOOGLE_BOOKS_API_KEY
    try:
        logger.info(f'Requesting books for genre: {genre_name}')
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=subject:{genre_name}&key={api_key}')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to fetch books for genre: {genre_name}, Error: {e}')
        return JsonResponse({f'error': 'Failed to fetch books'}, status=500)
    response=requests.get(f'https://www.googleapis.com/books/v1/volumes?q=subject:{genre_name}&key={api_key}')


    if response.status_code == 200:
        books = response.json().get('items', [])
        logger.info(f'Fetched {len(books)} books for genre: {genre_name}')
        return JsonResponse({'books':books})
    else:
        logger.error(f'Failed to fetch books for genre: {genre_name}, Status Code: {response.status_code}')
        return JsonResponse ({'error': 'Failed to fetch books'}, status=response.status_code)
    
def fetch_books_page(request):
    return render(request,'books/fetch_books.html')

def recommended_books(request):
    user_genres=UserGenre.objects.filter(user=request.user)
    books=[]
    for user_genre in user_genres:
        genre_name=user_genre.genre.name
        books.extend(get_books_by_genre(genre_name))
    return render(request,'books/recommended_books.html',{'books':books})
# Create your views here.
