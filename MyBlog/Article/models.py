from django.db import models


# Create your models here.
class Article(models.Model):
    Author = models.CharField(max_length=20)  # the author of blog
    title = models.CharField(max_length=100)  # the title of blog
    content = models.TextField(blank=True, null=True)  # the content of blog
    date = models.DateTimeField(auto_now_add=True)  # the time of creating blog
    tag = models.CharField(max_length=50, blank=True)  # the tag of bolg

    def __str__(self):
        return self.title
