from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail', detail, name='detail'),
    path('login', login, name='login'),
    path('search', search, name='search'),
    path('api/category/',getCategory,name='get-category')
    
]