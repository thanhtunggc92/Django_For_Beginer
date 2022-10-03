
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import AuthenticationForm

from .models import Post
from .forms import BlogCreate,BlogEdit,RegisterForm
# Create your views here.

def BlogPost(request):
    blog=Post.objects.all()
    context={'blog':blog}

    return render(request,'home.html',context)

def PostDetail(request,pk):
    blog=Post.objects.get(id=pk)

   
    context={'blog':blog}
    return render(request,'post_detail.html',context)

def BlogCreateView(request):
    context={}
    new_post=BlogCreate(request.POST or None)
    if request.method=='POST':
        
        if new_post.is_valid():
           

            new_post.save()
            return redirect ('home')
        else:
            return HttpResponse("""Your form is wrong""")
    context['form']=new_post
    return render (request,'post_new.html',context)


def EditBlog(request,pk):
    context={}
    blog_id=get_object_or_404(Post,id=pk)
    form= BlogEdit(request.POST or None, instance=blog_id)
    
    if form.is_valid():
            form.save()
            return redirect('home')
      
    context['form']=form
    return render(request,'edit_new.html',context)




def DeleteBlog(request,pk):
    post=Post.objects.get(id=pk)
    data=Post.objects.all()
    context={}
    context['title']=data
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render (request,'delete_new.html',context)






def LoginPage(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.info(request,f'You are log in as {username}')
            return redirect('home')
        else:
            messages.error(request,'Your username or password are incorrect!!')
    else:
       messages.error(request,'Your username or password are incorrect!!')
    form=AuthenticationForm()
    context={'form':form}
    return render (request,'login_form.html',context)

def Register(request):
    form=RegisterForm

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(f'You are created your account {user}')
            return redirect('loginforms')
        else:
            return 
    else:
        context={'form':form}
        return render (request,'register.html',context)

def LogoutPage(request):
    logout(request)
    messages.info(request,'You have successsfully logged out.')
    return redirect('home')