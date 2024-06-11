from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Writing(models.Model):
    title=models.CharField(max_length=200,help_text="Use Camel Case Only")
    blurb=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file=models.FileField(upload_to='create_novel/',blank=True,null=True)


    def __str__(self):
        return self.title
# Create your models here.
