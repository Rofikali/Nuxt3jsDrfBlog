# from pydoc import importfile
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    Serializer
)
from .models import Post
# from api_accounts.serializsers import ProfileSerializer
# from users.models import Profile

# class PostCreateSerializer(ModelSerializer):

#     class Meta:
#         model = Post
#         fields = [
#             'title', 'content', 'date_posted', 'author'
#         ]

#     author = SerializerMethodField()

#     def get_author(self, obj):
#         return obj.author.username


class PostListSerializer(ModelSerializer):

    detail_url = HyperlinkedIdentityField(
        view_name='api_blogs:detail',
        lookup_field='pk'
    )

    author_url = HyperlinkedIdentityField(
        view_name='api_blogs:particular-user-posts',
        lookup_field='author'
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author', 'author_url', 'detail_url'
        ]

    author = SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author'
        ]

    author = SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username


# class PostUpdateSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = [
#             'id', 'title', 'content', 'date_posted', 'author'
#         ]
#     author = SerializerMethodField()

#     def get_author(self, obj):
#         return obj.author.username
