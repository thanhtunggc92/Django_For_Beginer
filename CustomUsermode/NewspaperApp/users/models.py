from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):

    age=models.PositiveIntegerField(null=True,blank=True)
    

    def __str__(self):
        return str(self.username)