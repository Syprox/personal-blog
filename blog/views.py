from django.shortcuts import render
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic

def blog_index(request):
    """posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)"""

    posts = Post.objects.filter(status=1).order_by('-created_on')
    pages = Paginator(posts, 3)
    # 2 posts in each page
    page_number = request.GET.get('page')
    
    try:
        post_list = pages.page(page_number)
        print('Try worked')
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = pages.page(1)
        print('Exception 1')
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = pages.page(pages.num_pages)
        print('Exception 2')
    return render(request,
                  'blog/index.html',
                  {'page': page_number,
                   'posts': post_list})

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category, status=1
    ).order_by("-created_on")
    pages = Paginator(posts, 2)
    # 2 posts in each page
    page_number = request.GET.get('page')
    
    try:
        post_list = pages.page(page_number)
        print('Try worked')
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = pages.page(1)
        print('Exception 1')
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = pages.page(pages.num_pages)
        print('Exception 2')
    return render(request,
                  'blog/category.html',
                  {'page': page_number,
                   'category': category,
                   'posts': post_list})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)