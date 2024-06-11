from django import forms
from .models import Writing


class WritingForm(forms.ModelForm):
    class Meta:
        model=Writing
        fields=['title','blurb','file']


class SelectNovelForm(forms.Form):
    novel = forms.ChoiceField(label='Select a novel to edit')

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['novel'].choices = [(novel.pk, novel.title) for novel in Writing.objects.filter(user=user)]