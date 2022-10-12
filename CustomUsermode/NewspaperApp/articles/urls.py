from django.urls import path

from .views import AriticleListView,UpdateArticle,DeleteArticle,CreateArticle,ArtiicleDetail



urlpatterns=[
    path('',AriticleListView,name='article_list'),
    path('<str:pk>/edit/',UpdateArticle,name='article_edit'),
    path('<str:pk>/delete/',DeleteArticle,name='article_delete'),
    path('new/',CreateArticle,name='article_create'),
    path('<str:pk>',ArtiicleDetail,name='article_detail'),
]