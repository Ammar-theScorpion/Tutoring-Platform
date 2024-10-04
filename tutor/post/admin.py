from django.contrib import admin

from .models import Post
from .models import Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
