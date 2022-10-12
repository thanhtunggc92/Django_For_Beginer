from django.urls import path
from . import views
urlpatterns=[
    path('',views.HomePage,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.RegisterPage,name='signup'),
    path('logout/',views.LogoutPage,name='logout')

]