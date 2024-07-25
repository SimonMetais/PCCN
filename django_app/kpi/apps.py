from django.apps import AppConfig


class KpiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kpi'

    def ready(self):
        from .signals import session_deleted
