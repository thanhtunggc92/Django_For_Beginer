from multiprocessing import context
from django.shortcuts import render
from .models import Post
# Create your views here.


def PostMess(request):
    mess = Post.objects.all()
    
    context ={'mess':mess}

    return render(request,'home.html',context)