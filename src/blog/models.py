from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    author = models.OneToOneField(User, verbose_name="Автор")
    name = models.TextField(verbose_name="Название блога", max_length=255)
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменен", auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок поста", max_length=255)
    text = models.TextField(verbose_name="Текст")
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменен", auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class UserSubscribe(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменен", auto_now=True)

    def __str__(self):
        return "{} подписан на {}".format(self.user, self.blog)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class PostRead(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменен", auto_now=True)

    def __str__(self):
        return "{} прочитан пользователем {}".format(self.post, self.user)

    class Meta:
        verbose_name = 'Прочитанный пост'
        verbose_name_plural = 'Прочитанные посты'
