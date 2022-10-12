from re import template
from django.urls import path
from .views import HomePageView,PasswordChange,PasswordChangeDone
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',HomePageView,name='home'),
    path('password_change/',PasswordChange,name='password-change'),
    path('password_change/done',PasswordChangeDone,name='password-done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name ='password_reset'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]