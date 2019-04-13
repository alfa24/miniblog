from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from .models import Post, Blog, PostRead, UserSubscribe


class UserAuthenticatedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.user = request.user
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['current_user'] = self.user
        return context


# создание нового поста
class PostCreateView(UserAuthenticatedMixin, CreateView):
    user = None
    model = Post
    fields = ['title', 'text', 'blog']
    template_name = "blog/postcreate.html"
    success_url = '/feed'

    def get_initial(self):
        initial = super().get_initial()
        initial['blog'] = self.user.blog.id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django import forms
        form.fields["blog"].widget = forms.HiddenInput()
        return form


# лента новостей пользователя
class PostListView(UserAuthenticatedMixin, ListView):
    model = Post
    ordering = ['-created_at']
    fields = ['title', 'text']
    template_name = "blog/feed.html"

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        post = Post.objects.filter(id=post_id).first()
        if post:
            PostRead.objects.create(user=self.user, post=post)

        return super().get(request, *args, **kwargs)


# список всех блогов
class BlogListView(UserAuthenticatedMixin, ListView):
    model = Blog
    ordering = ['-created_at']
    fields = ['author', 'name', 'description']
    template_name = "blog/blog_list.html"

    def post(self, request, *args, **kwargs):
        blog_id = request.POST.get('blog_id')
        subscribe = request.POST.get('subscribe')
        blog = Blog.objects.filter(id=blog_id).first()
        if blog:
            if subscribe:
                UserSubscribe.objects.update_or_create(user=self.user, blog=blog)
            else:
                UserSubscribe.objects.filter(user=self.user, blog=blog).delete()

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.exclude(author=self.user)
        return qs





