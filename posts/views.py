from django.shortcuts import render, HttpResponse, redirect
from posts.forms import PostCreateForm
import posts
from posts.models import Post


def main_view(request):
    if request.method == "GET":
        return render(request, "main.html")
    else:
        pass

def posts_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "post_detail.html", context={"post": post})


def post_create_view(request):
    if request.method == "GET":
        form = PostCreateForm()
        return render(request, "post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "post_create.html", context={"form": form})
        elif form.is_valid():
            form.save()
            return redirect("/posts/")