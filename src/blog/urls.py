from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView

urlpatterns = [
    path('post/create', PostCreateView.as_view(), name='post_create'),
]
