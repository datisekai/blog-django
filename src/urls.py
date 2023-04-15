from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>/', detail, name='detail'),
    path('login', login, name='login'),
    path('search', search, name='search'),
    path('logout/', logout_view, name='logout'),
    path('api/category/', getCategory, name='get-category'),
    path('api/comment/<slug:slug>/', getCommentAndReact, name='get-comment-react'),
    path('api/comment', addComment, name='add-comment'),
    path('api/comment/delete/<int:id>', deleteComment, name='delete-comment'),
    path('api/comment/update/<int:id>', updateComment, name='update-comment'),
    path('api/react/<int:id>', addLike, name='add-like')
]
