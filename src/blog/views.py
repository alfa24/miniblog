from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from .models import Post, Blog


class PostCreateView(LoginRequiredMixin, CreateView):
    user = None
    model = Post
    fields = ['title', 'text', 'blog']
    template_name = "blog/postcreate.html"
    success_url = '/feed'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.user = request.user
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['blog'] = self.user.blog.id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django import forms
        form.fields["blog"].widget = forms.HiddenInput()
        return form


