from django.shortcuts import render
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ImageForm

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

    posts = Post.objects.filter(category__name__contains=category, status=1).order_by("-created_on")
    posts_on_page = 2
    page_number = request.GET.get('page')

    context = {'page': page_number,
               'category': category,
               'posts': get_posts_list(posts, page_number, posts_on_page)}
    
    return render(request,
                  'blog/category.html',
                  context)

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                message=form.cleaned_data["message"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    print("Вибраний допис: " + str(post.post_id))
    comments = Comment.objects.filter(post=post)
    
    context = {
        "post": post,
        "comments": comments,
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

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'blog/image_upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
        return render(request, 'blog/image_upload.html', {'form': form})