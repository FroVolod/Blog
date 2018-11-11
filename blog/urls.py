from django.urls import path

from .views import posts_list, tags_list
from .views import PostCreate, TagCreate
from .views import PostDetail, TagDetail
from .views import PostDelete, TagDelete
from .views import PostUpdate, TagUpdate

urlpatterns = [
    path('posts/', posts_list, name='posts_list_url'),
    path('posts/create/', PostCreate.as_view(), name='post_create_url'),
    path('posts/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('posts/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('posts/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tags/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:slug>/delete', TagDelete.as_view(), name='tag_delete_url'),
]

