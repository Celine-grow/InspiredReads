from django import forms
from .models import Genre

class GenreSelectionForm(forms.Form):
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple,required=True)