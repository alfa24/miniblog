from django.contrib import admin
from django.urls import path

import blog

urlpatterns = [
    path('', blog.urls),
]
