# users/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserGenre(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.genre.name}"


# Create your models here.
