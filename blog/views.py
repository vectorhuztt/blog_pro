from django.shortcuts import render
from .models import Post, Tag, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        posts, tag = Post.get_by_tag(tag_id)
    elif category_id:
        posts, category = Post.get_by_category(category_id)
    else:
        posts = Post.latest__posts()

    context = {
        'category': category,
        'tag': tag,
        'sidebars': SideBar().get_all(),
        'post_list': posts
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'sidebars': SideBar().get_all(),
        'post': post,
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context={'post': post})


def links(request):
    # return HttpResponse('links')
    return render(request, 'blog/link.html', context={'name': 'link'})