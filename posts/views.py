from django.shortcuts import render, HttpResponse

import posts
from posts.models import Post


def main_view(request):
    return render(request, "main.html")

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", context={"post": post})
