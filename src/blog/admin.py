from django.contrib import admin

from .models import Post, Blog, UserSubscribe, PostRead

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(UserSubscribe)
admin.site.register(PostRead)
