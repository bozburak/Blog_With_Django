# *-*coding:utf-8*-*
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_index(request):
    posts = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            'name': 'Admin',
            'posts': posts
        }
    else:
        context = {
            'name': 'Misafir',
            'posts': posts
        }
    return render(request, 'Posts.html', context)

def post_detail(request, id):
    posts = get_object_or_404(Post, id=id)
    context = {
        'posts': posts
    }
    return render(request, 'Detail.html', context)