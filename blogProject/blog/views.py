# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()[:10]
    context = {
        'posts' : posts
    }
    return render(request, 'home.html', context)

def post(request, url):
    post = Post.objects.get(url = url)
    data = {
        'post' : post
    }
    return render(request, 'post.html', data)