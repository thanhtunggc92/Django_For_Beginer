
from django.utils import timezone

from django.db import models
from django.contrib.auth import get_user_model
from django .conf import settings
from django.urls import reverse



class Articles(models.Model):

    title=models.CharField(max_length=255)
    body= models.TextField(max_length=200, blank=True, default=None)
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    article=models.ForeignKey(Articles, on_delete= models.CASCADE,related_name='comments')
    comment=models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)


    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')

 