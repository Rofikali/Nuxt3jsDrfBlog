from rest_framework import serializers
from api.models import Posts


class PostListSerializer(serializers.ModelSerializer):
    slug = serializers.HyperlinkedIdentityField(
        view_name='apis:detail',
        lookup_field='pk'
    )
    author = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'title', 'slug', 'content',
                  'author', 'date_created', 'date_updated'
                  ]

    def get_author(self, obj):
        return obj.author.name
