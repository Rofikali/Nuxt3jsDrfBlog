
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    # SerializerMethodField
)
from .models import PythonModel


class PythonSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='python:python',
        lookup_field='pk'
        # lookup_field='category'
    )

    class Meta:
        model = PythonModel
        fields = ['id', 'slug', 'title', 'detail_url', 'content',
                  'date_created', 'date_updated']
        # fields = ['title','slug', 'content']


# class CategoryListSerializer(ModelSerializer):

#     detail_url = HyperlinkedIdentityField(
#         view_name='api_courses:category',
#         lookup_field='pk'
#         # lookup_field='category'
#     )

#     # category_url = HyperlinkedIdentityField(
#     #     view_name='api_courses:particular-categories',
#     #     lookup_field='category'
#     # )

#     class Meta:
#         model = CategoryList
#         fields = [
#             'id', 'name', 'category', 'content', 'detail_url', 'date_created', 'date_updated'
#         ]
#         # fields = [
#         #     'id', 'name', 'category', 'category_url', 'content', 'detail_url', 'date_created', 'date_updated'
#         # ]

#     category = SerializerMethodField()

#     def get_category(self, obj):
#         return obj.category.name


# # class PostDetailSerializer(ModelSerializer):
# #     class Meta:
# #         model = Post
# #         fields = [
# #             'id', 'title', 'content', 'date_posted', 'author'
# #         ]

# #     author = SerializerMethodField()

# #     def get_author(self, obj):
# #         return obj.author.username


# class CategorySerializer(ModelSerializer):
#     category_url = HyperlinkedIdentityField(
#         view_name='api_courses:particular-categories',
#         lookup_field='category'
#     )

#     class Meta:
#         model = CategoryList
#         fields = [
#             'id', 'category', 'category_url', 'date_created', 'date_updated'
#         ]

#     category = SerializerMethodField()

#     def get_category(self, obj):
#         return obj.category.name