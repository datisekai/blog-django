from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', home, name='home'),
    path('detail', detail, name='detail'),
    path('login', custom_login, name='login'),
    path('search', search, name='search'),
    path('api/category/', getCategory, name='get-category'),

]
