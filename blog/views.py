from django.shortcuts import render, get_object_or_404

from .models import Post, Author, Tag

def starting_page(request):
    
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    
    all_posts = Post.objects.all().order_by("-date") # oden decendente

    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": post
    })
    
def authors(request):
    
    authors = Author.objects.all()

    return render(request, "blog/authors_list.html", {
        "authors": authors
    })

def author_detail(request, id):
    
    author = get_object_or_404(Author, pk=id)

    return render(request, "blog/author_detail.html", {
        "author": author
    })
    
def tags(request):
    
    tags = Tag.objects.all()

    return render(request, "blog/tag_list.html", {
        "tags": tags
    })

def tag_posts(request, id):
    
    tag = get_object_or_404(Tag, pk=id)

    posts = tag.post_set.all()

    return render(request, "blog/tag_post.html", {
        "tag": tag,
        "posts": posts
    })
    
def handler404(request, exception):
    return render(request, "blog/404.html", status=404)
