from django.conf import settings
from django.core.mail import send_mail


# todo подключить Celery
def send_mail_task(theme, message, mails):
    print("Отправка сообщения на emails: {} ".format(mails))
    try:
        send_mail(theme, message, settings.EMAIL_HOST_USER, mails)
    except Exception as e:
        print(e)
