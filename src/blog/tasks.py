from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_task(param):
    try:
        theme = param['theme']
        message = param['message']
        mails = param['mails']
    except Exception as e:
        print(e)
        return
    print("Отправка сообщения на emails: {} ".format(mails))
    send_mail(theme, message, settings.EMAIL_HOST_USER, mails)


