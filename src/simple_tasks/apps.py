from django.apps import AppConfig


class SimpleTasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simple_tasks'

    def ready(self) -> None:
        from simple_tasks import tasks
