from django.shortcuts import render
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def blog_index(request):

    posts = Post.objects.filter(status=1).order_by('-created_on')
    posts_on_page = 3
    page_number = request.GET.get('page')

    context = {'page': page_number,
               'posts': get_posts_list(posts, page_number, posts_on_page)}

    return render(request,
                  'blog/index.html',
                  context)

def blog_category(request, category):

    posts = Post.objects.filter(categories__name__contains=category, status=1).order_by("-created_on")
    posts_on_page = 2
    page_number = request.GET.get('page')

    context = {'page': page_number,
               'category': category,
               'posts': get_posts_list(posts, page_number, posts_on_page)}
    
    return render(request,
                  'blog/category.html',
                  context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["message"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    all_comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": all_comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)

def get_posts_list (posts, page_number, posts_on_page):
    pages = Paginator(posts, posts_on_page)
    
    try:
        posts_list = pages.page(page_number)
        print('Try worked')
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        posts_list = pages.page(1)
        print('Exception 1')
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts_list = pages.page(pages.num_pages)
        print('Exception 2')

    return posts_list