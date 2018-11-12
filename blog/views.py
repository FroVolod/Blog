from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse


from .forms import PostForm, TagForm
from .models import Post, Tag
from .utils import ObjectCreateMixin, ObjectDetailMixin, ObjectUpdateMixin, ObjectDeleteMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_template = 'posts_list_url'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_template = 'tags_list_url'
