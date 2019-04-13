from django import template

from ..models import PostRead, Blog, UserSubscribe

register = template.Library()


@register.simple_tag(takes_context=True)
def post_is_read(context, post):
    user = context.get('current_user', None)
    result = PostRead.objects.filter(user=user, post=post)

    return result.exists()


@register.simple_tag(takes_context=True)
def is_subscribe_blog(context, blog):
    user = context.get('current_user', None)
    result = UserSubscribe.objects.filter(user=user, blog=blog)

    return result.exists()
