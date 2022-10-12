from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Articles,Comment
from .forms import ArticleForm,ArticleCreate
from django.contrib import messages



def AriticleListView(request):
    model=Articles.objects.all()
    comments=Comment.objects.all()
    context={'model':model,'comments':comments}
    return render (request,'articles/article_list.html',context)

@login_required()
def UpdateArticle(request,pk):
   
    article_id = Articles.objects.get(id=pk)
    if request.method =='POST':
        form=ArticleForm(request.POST or None,instance= article_id)
        if form.is_valid():
            form.save()
            # article.UpdateArticle=request.user
            # article.save()
            return redirect('article_list')
    else:
         form=ArticleForm()
    context={'form':form}
    return render(request,'articles/article_edit.html',context)

@login_required()
def DeleteArticle(request,pk):
    article_id= Articles.objects.get(id=pk)
    data=Articles.objects.all()
    if request.method =='POST':
        article_id.delete()
        return redirect('article_list')
    context={'data':data}
    return render (request,'articles/article_delete.html',context)

def CreateArticle(request):
    new_article=ArticleCreate()
    if request.method=='POST':
        new_article=ArticleCreate(request.POST or None)
        if new_article.is_valid():
            new_article.save()
            return redirect('article_list')
        else:
            messages.error(request,"You are in wrong Form")
   
      
    context={'new_article':new_article}

    return render(request,'articles/article_create.html',context)


def ArtiicleDetail(request,pk):

    form=Articles.objects.get(id=pk)
    context={'form':form}

    return render (request,'articles/article_detail.html',context)  


