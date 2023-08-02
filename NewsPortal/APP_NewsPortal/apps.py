from django.apps import AppConfig


class AppNewsportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APP_NewsPortal'

    def ready(self):
        from . import signals
