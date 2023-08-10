from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.utils import timezone


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all().filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True).order_by('pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.all().filter(
                             pub_date__lte=timezone.now(),
                             is_published=True,
                             category__is_published=True), pk=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category_in_posts = get_object_or_404(Category, slug=category_slug,
                                   is_published=True)
    post_list = Post.objects.all().filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
        category=category_in_posts
    )
    
    context = {'category': category_in_posts,
               'post_list': post_list}
    return render(request, template, context)
