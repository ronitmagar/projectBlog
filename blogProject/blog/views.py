# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()[:10]
    data = {
        'posts' : posts
    }
    return render(request, 'home.html', data)

def post(request, url):
    # posts = Post.objects.get(url = url)
    data = {
        'url' : url
    }
    return render(request, 'post.html', data)