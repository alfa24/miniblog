from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .tasks import send_mail_task
from .models import Post, UserSubscribe


def post_create_handler(sender, instance, created, **kwargs):
    if created:
        user_ids = list(UserSubscribe.objects.filter(blog=instance.blog).values_list('user_id', flat=True))
        users = User.objects.filter(pk__in=user_ids)

        if not users.exists():
            return

        theme = "{} разместил новый пост".format(instance.blog.author.username)
        message = instance.title
        mails = list(users.values_list('email', flat=True))
        send_mail_task(theme=theme, message=message, mails=mails)


post_save.connect(post_create_handler, sender=Post)

