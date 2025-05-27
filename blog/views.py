from django.shortcuts import render
from .models import Post, Author, Tag

# Create your views here.
def starting_page(request):
    try:
        posts = Post.objects.order_by("-date")
        return render(request, "blog/index.html", {
            "posts": posts,
        })
    except:
        return render(request, "blog/404.html", status=404)

def posts(request):
    try:
        posts = Post.objects.all().order_by("-date")
        return render(request, "blog/posts.html", {
            "posts": posts,
        })
    except:
        return render(request, "blog/404.html", status=404)
    
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post_detail.html", {"post": post})
    except:
        return render(request, "blog/404.html", status=404)

def authors(request):
    try:
        authors = Author.objects.all().order_by("last_name")
        return render(request, 'blog/authors.html', {
            "authors": authors,
        })
    except:
        return render(request, 'blog/404.html', status=404)

def author_detail(request, first_name, last_name):
    try:
        author = Author.objects.get(first_name=first_name, last_name=last_name)
        posts = author.posts.all()
        return render(request, 'blog/author_detail.html', {
            "author": author,
            "posts": posts,
        })
    except:
        return render(request, 'blog/404.html', status=404)

def tags(request):
    try:
        tags = Tag.objects.all()
        return render(request, 'blog/tags.html', {
            "tags": tags,
        })
    except:
        return render(request, 'blog/404.html', status=404)

def tag_detail(request, tag):
    try:
        tag = Tag.objects.get(tag=tag)
        posts = tag.posts.all()
        return render(request, 'blog/tag_detail.html', {
            "tag": tag,
            "posts": posts,
        })
    except:
        return render(request, 'blog/404.html', status=404)