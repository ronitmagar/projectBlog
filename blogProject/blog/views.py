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
    posts = Post.objects.all()
    urls = [(post.url,post.title) for post in posts]
    post = Post.objects.get(url = url)
    allpost = Post.objects.get
    data = {
        'urls' : urls,
        'post' : post
    }
    return render(request, 'post.html', data)

def about(request):
    return render(request, 'about.html')