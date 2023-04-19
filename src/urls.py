from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', home, name='home'),
    path('detail', detail, name='detail'),
    path('login', custom_login, name='login'),
    path('user/login/', isLogin, name='login'),
    path('register', custom_register, name='custom_register'),
    path('search', search, name='search'),
    path('api/category/', getCategory, name='get-category'),
    path('user/add/', isResister, name="addUser"),
    path('forgetpassword', custom_forgetpassword, name="custom_forgetpassword"),
    path('forgetpassword/sendemail/', forgetPassword,
         name="custom_forgetpassword"),
    path('change_password/<token>/', ChangePasswordToken,
         name="ChangePasswordToken"),
    path('change_password/<token>/changepassword/',
         ChangePassword, name="ChangePassword")
]
