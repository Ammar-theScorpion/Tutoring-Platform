import uuid

from django.db import models
from utils.model import TimeStampModel


class Post(TimeStampModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image_url = models.URLField()

    def __str__(self) -> str:
        return self.title
