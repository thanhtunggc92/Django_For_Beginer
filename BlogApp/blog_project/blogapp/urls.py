from distutils.log import Log
from django.urls import path
from .views  import  BlogPost, EditBlog,PostDetail,BlogCreateView,DeleteBlog,LoginPage,Register,LogoutPage

urlpatterns=[
    path('',BlogPost,name='home'),
    path('post/<str:pk>/',PostDetail,name='post'),
    path('post/new',BlogCreateView ,name='post-new'),
    path('update/<str:pk>/',EditBlog,name='update'),
    path('delete/<str:pk>',DeleteBlog,name ='delete'),
    path('loginform',LoginPage, name='login'),
    path('registerform',Register,name='register'),
    path('logout/',LogoutPage,name='logout')
]