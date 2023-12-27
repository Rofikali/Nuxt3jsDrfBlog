from api.models import Posts
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView
)

from .serializers import (PostListSerializer)


class HomeAPIView(ListAPIView):
    """
        List of all data.
    """
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer

    # def get_queryset(self):
    #     return super().get_queryset()


class DetailAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'pk'
