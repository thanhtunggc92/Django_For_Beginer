import re
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib.auth .forms import PasswordChangeForm

def HomePageView(request):
    context={}
    return render(request,'home.html',context)


def PasswordChange(request):
    form = PasswordChangeForm
    if request.method =="POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save() 
            update_session_auth_hash(request,user)
            messages.success(request,'Your password has been changed')
            return redirect ('password-done')

    else:
        form= PasswordChangeForm(user=request.user)
        context={'form':form}
        return render (request,'registration/password_change.html',context)


def PasswordChangeDone(request):
    context={}
    return render (request,'registration/password_change_done.html',context)