from django.db import models

# Create your models here.
class Post(models.Model):
    chat= models.TextField()

    def __str__(self):
        return self.chat[:50]