
from django.shortcuts import render,redirect
from .forms import CustomCreationForm,CustomChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def HomePage(request):
    context={}

    return render(request,'home.html',context)

def LoginPage(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'You are log in as {username}')
            return redirect ('home')
        else:
            messages.info(request,'username or password is incorrect!')
    
    context={'form':form}
    return render(request,'registration/login.html',context)

def RegisterPage(request):
    form = CustomCreationForm()
    if request.method=='POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
          
    context={'form':form}
    return render(request,'registration/signup.html',context)
def LogoutPage(request):
    logout(request)
    messages.info(request,'You are logout')
    return redirect ('home')
