# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-07-23 07:00
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230723_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]