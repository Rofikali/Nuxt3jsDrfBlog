from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api_blog.urls", namespace="api_blogs")),
    path("api/", include("api_courses.urls", namespace="api_courses")),
    path("api/", include("api_python.urls", namespace="python")),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
]
