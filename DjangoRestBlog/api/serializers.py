from rest_framework import serializers
from api.models import Posts


class PostListSerializer(serializers.ModelSerializer):
    slug = serializers.HyperlinkedIdentityField(
        view_name='apis:detail',
        lookup_field='pk'
    )

    class Meta:
        model = Posts
        fields = ['id',
                  'title',
                  'slug',
                  'content',
                  'author',
                  'date_created',
                  'date_updated'
                  ]

    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.name
