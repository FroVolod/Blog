from django.db import models
from django.utils.text import slugify

from time import time


def gen_slug(s):
    return slugify(s) + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    create_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title