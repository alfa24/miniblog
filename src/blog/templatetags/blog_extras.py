from django import template

from ..models import PostRead

register = template.Library()


@register.simple_tag(takes_context=True)
def post_is_read(context, post):
    user = context.get('current_user', None)
    result = PostRead.objects.filter(user=user, post=post)

    return result.exists()