from django.urls import path
from . import views
from .views import create_novel,edit_novel,select_novel
app_name="Novelwrite"
urlpatterns=[
    path('createNovel/',create_novel,name='create_novel'),
    path('selectNovel/', select_novel, name='select_novel'),
    path('editNovel/<int:pk>/',edit_novel,name='edit_novel'),
]