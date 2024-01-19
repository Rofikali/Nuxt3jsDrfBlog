from django.urls import path
from . views import (
    PostListApiView,
    PostRetrivApiView,
    # PostUpdateApiView,
    # PostDeleteApiView,
    # PostCreateApiView,
    # particular user's post
    PerticularUserPosts
)


app_name = 'api_blogs'

urlpatterns = [
    path('posts', PostListApiView.as_view(), name='list'),
    # path('create/', PostCreateApiView.as_view(), name='create'),
    path('posts/<int:pk>/', PostRetrivApiView.as_view(), name='detail'),
    # {
    # path('detail/<int:pk>/', PostRetrivApiView.as_view(), name='detail'),
    # }
    # path('update/<int:pk>/', PostUpdateApiView.as_view(), name='update'),
    # path('delete/<int:pk>/', PostDeleteApiView.as_view(), name='delete'),
    # # particular user's post
    path('user/<str:author>', PerticularUserPosts.as_view(),
         name='particular-user-posts'),
]
