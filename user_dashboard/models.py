import uuid
from django.db import models
from users.models import CustomUser


class BrowserBox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f"{self.ip}|{self.owner}"

    class Meta:
        verbose_name = "browser_box"
        verbose_name_plural = "browser_boxes"
        ordering = ["id", ]
