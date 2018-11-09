from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse


from .forms import PostForm, TagForm
from .models import Post, Tag
from .utils import ObjectCreateMixin, ObjectDetailMixin


def posts_list(request):
    return render(request, 'blog/posts_list.html')


def tags_list(request):
    return render(request, 'blog/tags_list.html')


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'