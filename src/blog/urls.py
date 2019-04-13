from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView, PostListView, BlogListView, BlogEditView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('blog/', BlogEditView.as_view(), name='blog_edit'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('feed/', PostListView.as_view(), name='feed'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
]
