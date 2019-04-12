from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from .models import Post, Blog, PostRead


class UserAuthenticatedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.user = request.user
        return super().dispatch(request, *args, **kwargs)


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['current_user'] = self.user
        return context




