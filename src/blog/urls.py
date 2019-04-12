from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView, PostListView

urlpatterns = [
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('feed/', PostListView.as_view(), name='feed'),
]
