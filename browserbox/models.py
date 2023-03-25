import datetime
import uuid
from django.db import models


def _add_30_minutes():
    return datetime.datetime.now() + datetime.timedelta(minutes=30)


class BrowserBox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    create_dt = models.DateTimeField(default=datetime.datetime.now)
    terminate_dt = models.DateTimeField(default=_add_30_minutes)

    def __str__(self):
        return f"{self.ip}"

    class Meta:
        verbose_name = "browser_box"
        verbose_name_plural = "browser_boxes"
        ordering = ["id", ]


class HistoryBrowserBox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    create_dt = models.DateTimeField(default=datetime.datetime.now)
    terminate_dt = models.DateTimeField(default=_add_30_minutes)

    def __str__(self):
        return f"{self.ip}"

    class Meta:
        verbose_name = "history_browser_box"
        verbose_name_plural = "history_browser_boxes"
        ordering = ["id", ]


class Worker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"
        ordering = ["id", ]

