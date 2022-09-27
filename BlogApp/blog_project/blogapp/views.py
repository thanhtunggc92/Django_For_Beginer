
from django.shortcuts import render
from .models import Post
# Create your views here.

def BlogPost(request):
    blog=Post.objects.all()
    context={'blog':blog}

    return render(request,'home.html',context)

def PostDetail(request,pk):
    blog=Post.objects.get(id=pk)

   
    context={'blog':blog}
    return render(request,'post_detail.html',context)

