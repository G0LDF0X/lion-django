from django.db import models

# Create your models here.
# title, url

class Bookmark(models.Model):
    # blank : 공백을 허용하면 True
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    def __str__(self):
        return self.title + " " + self.url
