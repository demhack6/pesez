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


class BrowserBoxSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    user_agent = models.TextField(blank=False)
    last_active = models.DateTimeField()
    browser_box = models.ForeignKey(BrowserBox, on_delete=models.CASCADE)

    def __str__(self):
        # Choose better repr option.
        return f"{self.id}"

    class Meta:
        verbose_name = "browser_box_session"
        verbose_name_plural = "browser_box_sessions"
        ordering = ["id", ]
