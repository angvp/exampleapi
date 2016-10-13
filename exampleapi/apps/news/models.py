from __future__ import unicode_literals

from django.db import models

from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
