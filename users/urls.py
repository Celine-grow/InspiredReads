from django.urls import path
from .views import register,profile,CustomLoginView,dashboard

app_name="users"
urlpatterns=[
    path('register/',register,name='register'),
    path('profile/<str:username>/',profile,name='profile'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('dashboard/',dashboard,name='dashboard'),
]