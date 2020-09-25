from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from .models import *


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post,
    }
    return render(request, 'main/post_template.html', context)


def blog(request):
    posts = Post.objects.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    tags = Tag.objects.all()
    crumb = 'Блог'

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'crumb': crumb,
        'tags': tags,
    }
    return render(request, 'main/blog.html', context)