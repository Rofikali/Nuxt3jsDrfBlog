from django.urls import path
from . views import (
    PythonListAPIView,
    PythonRetrieveAPIView
)


app_name = 'python'

urlpatterns = [
    path("python", PythonListAPIView.as_view(), name="list_python"),
    path("python/<int:pk>/", PythonRetrieveAPIView.as_view(), name="python")
    # path('categories/', CategoryListApiView.as_view(), name='categories'),
    # # path('categories/<str:category>/<int:pk>/', CategoryRetrivApiView.as_view(), name='category'),
    # path('categories/category/<int:pk>/', CategoryRetrivApiView.as_view(), name='category'),
    # # particular user's post
    # path('categories/<str:category>', PerticularCategoryApiView.as_view(),
    #      name='particular-categories'),
]
