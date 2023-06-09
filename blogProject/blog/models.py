# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    Category_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.CharField(max_length = 100)
    
