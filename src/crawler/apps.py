from django.apps import AppConfig


class CrawlerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "crawler"

    def ready(self) -> None:
        from crawler import tasks
