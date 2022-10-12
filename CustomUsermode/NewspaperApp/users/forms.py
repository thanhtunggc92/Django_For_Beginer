
from .models import CustomUser

from django.contrib.auth.forms import UserChangeForm,UserCreationForm


class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model= CustomUser
        fields=['username','email','age']

class CustomChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['username','email','age']