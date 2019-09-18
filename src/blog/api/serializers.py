from rest_framework.serializers import ModelSerializer
from blog.models import BlogPost


class PostListSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
        ]


class PostCreateEditSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'publish_date',
            'image',
            'slug'
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'timestamp',
            'image'
        ]
