from django.urls import path

from .views import posts_list
from .views import PostCreate
from .views import PostDetail

urlpatterns = [
    path('posts/', posts_list, name='posts_list_url'),
    path('posts/create/', PostCreate.as_view(), name='post_create_url'),
    path('posts/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
]

