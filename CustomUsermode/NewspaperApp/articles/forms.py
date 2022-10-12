from operator import mod
from .models import Articles
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:

        model=Articles
        fields=['title','body']


class ArticleCreate(forms.ModelForm):
    class Meta:
        model=Articles
        fields='__all__'

        