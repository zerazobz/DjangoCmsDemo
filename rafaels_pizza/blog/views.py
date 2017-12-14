from django.shortcuts import render
from .models import *

def post(request, p_id):
    selectedPost = Post.objects.get(pk=p_id)
    context = {}
    context["post"] = selectedPost

    return render(request, "post.html", context)

def category(request, c_id):
    context = {}
    selectedCategory = Category.objects.get(pk=c_id)
    context["category"] = selectedCategory

    posts = Post.objects.filter(category = selectedCategory)
    context["post"] = posts

    return render(request, "category.html", context)

def blog(request):
    context = {}
    posts = Post.objects.all()
    context["posts"] = posts

    return render(request, "blog.html", context)