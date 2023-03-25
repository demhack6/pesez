import datetime
import uuid
from django.db import models

WORKER_STATUS_CHOICES = (
    ('AV', 'Available'),
    ('BS', 'Busy'),
    ('RS', 'Requested to shut down'),
    ('SH', 'Shutting down'),
    ('RI', 'Requested to initalize'),
    ('IN', 'Initializing'),
)


def _add_30_minutes():
    return datetime.datetime.now() + datetime.timedelta(minutes=30)


class BrowserBox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    create_dt = models.DateTimeField(default=datetime.datetime.now)
    terminate_dt = models.DateTimeField(default=_add_30_minutes)
    archived = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.ip}"

    class Meta:
        verbose_name = "browser_box"
        verbose_name_plural = "browser_boxes"
        ordering = ["id", ]
        indexes = [
            models.Index(
                'id',
                condition=models.Q(archived__eq=False),
                name='active_browser_boxes_idx',
            )
        ]


class Worker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    status = models.CharField(
        max_length=2,
        choices=WORKER_STATUS_CHOICES,
        default='RI',
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"
        ordering = ["id", ]

