from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from .models import Category, CategoryList
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from . serializers import (
    CategoryListSerializer,
    CategorySerializer
    # PostDetailSerializer,
)


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = CategoryList.objects.all()

        # Get unique categories
        categories = Category.objects.all()

        # Retrieve one post per author
        unique_categories = []
        for category in categories:
            name_category = queryset.filter(category=category).first()
            if name_category:
                unique_categories.append(name_category)

        return unique_categories


class PerticularCategoryApiView(ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        category_name = get_object_or_404(
            Category, name=self.kwargs.get('category'))
        return CategoryList.objects.filter(category=category_name)
        # return CategoryList.objects.filter(category=category_name).order_by('-date_created')


class CategoryRetrivApiView(RetrieveAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer
