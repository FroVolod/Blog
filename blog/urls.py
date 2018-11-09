from django.urls import path

from .views import posts_list, tags_list
from .views import PostCreate, TagCreate
from .views import PostDetail, TagDetail

urlpatterns = [
    path('posts/', posts_list, name='posts_list_url'),
    path('posts/create/', PostCreate.as_view(), name='post_create_url'),
    path('posts/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
]

