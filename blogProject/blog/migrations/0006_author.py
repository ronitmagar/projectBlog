# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-08-03 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20230723_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='author/')),
            ],
        ),
    ]
