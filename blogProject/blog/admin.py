# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category, Post
from django.contrib import admin

# Register your models here.


class categoryAdmin(admin.ModelAdmin):
    list_display = ("image_display" ,"title", "url", "description", "add_date")
    search_fields = ('title',)

class postAdmin(admin.ModelAdmin):
    list_display = ("image_display", 'title')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50


admin.site.register(Category, categoryAdmin)
admin.site.register(Post, postAdmin)