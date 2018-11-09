from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse


from .forms import PostForm
from .models import Post


def posts_list(request):
    return render(request, 'blog/posts_list.html')


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, 'blog/post_create.html', context={'form': bound_form})


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})