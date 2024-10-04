import uuid

from django.contrib.auth import get_user_model
from django.db import models
from utils.model import TimeStampModel

User = get_user_model()


class Post(TimeStampModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image_url = models.URLField()

    author = models.ForeignKey(User, related_name="posts", on_delete=models.Case)
    tags = models.ManyToManyField("Tag")

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name
