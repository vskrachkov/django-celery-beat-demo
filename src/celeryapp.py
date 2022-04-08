import os
from typing import Any

from celery import Celery
from celery.signals import after_setup_logger
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

app = Celery("project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@after_setup_logger.connect
def config_loggers(*args: Any, **kwargs: Any) -> None:
    from logging.config import dictConfig
    from django.conf import settings

    dictConfig(settings.LOGGING)
