from django.urls import path
from .views  import BlogPost,PostDetail

urlpatterns=[
    path('',BlogPost,name='blog'),
    path('post/<str:pk>/',PostDetail,name='post')
]