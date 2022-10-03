

from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogCreate(forms.ModelForm):


    class Meta:
        model=Post
        fields='__all__'


class BlogEdit(forms.ModelForm):


    class Meta:
        model= Post
        fields=['title','body']

class RegisterForm(UserCreationForm):

    class Meta:
        model= User
        fields=['username','email','password1','password2']