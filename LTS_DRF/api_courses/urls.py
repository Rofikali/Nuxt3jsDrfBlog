from django.urls import path
from . views import (
    CategoryListApiView,
    PerticularCategoryApiView,
    CategoryRetrivApiView
)


app_name = 'api_blogs'

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories'),
    # path('categories/<str:category>/<int:pk>/', CategoryRetrivApiView.as_view(), name='category'),
    path('categories/category/<int:pk>/', CategoryRetrivApiView.as_view(), name='category'),
    # particular user's post
    path('categories/<str:category>', PerticularCategoryApiView.as_view(),
         name='particular-categories'),
]
