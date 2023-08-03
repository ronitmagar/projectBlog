# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    Category_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'category/')
    add_date = models.DateTimeField(auto_now_add = True, null = True)

    def image_display(self):
        return format_html('<img src = "/media/{}" style="width:40px;height:40px;border-radius:50%"/>'.format(self.image))

    def __str__(self):
        return self.title


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    occupation = models.CharField(max_length = 50)
    about = models.TextField()
    image = models.ImageField(upload_to = 'author/')

    def image_display(self):
        return format_html('<img src = "/media/{}" style="width:40px;height:40px;border-radius:50%"/>'.format(self.image))

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    content = HTMLField()
    url = models.CharField(max_length = 100)
    cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    # author = models.ForeignKey(Author, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'post/')
    

    def image_display(self):
        return format_html('<img src = "/media/{}" style="width:40px;height:40px;border-radius:50%"/>'.format(self.image))
    
    def __str__(self):
        return self.title
