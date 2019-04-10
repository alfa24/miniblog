from django.apps import AppConfig


class Config(AppConfig):
    name = 'blog'
    verbose_name = 'Блог'

    def ready(self):
        import blog.handlers