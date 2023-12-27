from rest_framework import status
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from django.contrib.auth.models import User
from .serializers import PostListSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    # RetrieveUpdateAPIView,
    # RetrieveDestroyAPIView,
    # CreateAPIView
)
from . serializers import (
    PostListSerializer,
    PostDetailSerializer,
    # PostUpdateSerializer,
    # PostCreateSerializer
)
from .models import Post
from .permissions import IsPostOwner
from .paginations import TestingOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, AllowAny

# listing perticular user's posts
User = get_user_model()


# class PostCreateApiView(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateSerializer
#     permission_classes = [IsAdminUser]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class PostListApiView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer
#     pagination_class = TestingOffsetPagination
#     filter_backends = [SearchFilter]
#     search_fields = ['content', 'title']


class PostListApiView(ListAPIView):
    serializer_class = PostListSerializer
    # pagination_class = TestingOffsetPagination
    # filter_backends = [SearchFilter]
    # search_fields = ['content', 'title']

    def get_queryset(self):
        queryset = Post.objects.all()

        # Get unique authors
        authors = User.objects.all()

        # Retrieve one post per author
        unique_posts = []
        for author in authors:
            author_post = queryset.filter(author=author).first()
            if author_post:
                unique_posts.append(author_post)

        return unique_posts
        # return Response(unique_posts, status=HTTP_200_OK)


class PostRetrivApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


# class PostUpdateApiView(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostUpdateSerializer
#     permission_classes = [IsPostOwner]

#     def perform_update(self, serializer):
#         return serializer.save(author=self.request.user)


class PerticularUserPosts(ListAPIView):
    # queryset = Post.objects.all()
    pagination_class = TestingOffsetPagination
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('author'))
        return Post.objects.filter(author=user).order_by('-date_posted')

        # user = get_object_or_404(User, username=self.kwargs.get('author'))
        # print()
        # print()
        # print(self.kwargs.get('author'))
        # print()
        # dic_data = self.kwargs
        # print()
        # print('............',dic_data)
        # for i in dic_data:
        #     print('inside print for loop', i)

        # a = {
        #     'a':'data',
        #     'b':'Mnago'
        # }
        # # print(a.items())
        # for i in a.items():
        #     print(i)

        # print()
        # print()
