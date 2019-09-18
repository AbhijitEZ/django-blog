from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateEditSerializer
from blog.models import BlogPost


class PostListAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostEditAPIView(UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostCreateEditSerializer
    lookup_field = 'slug'


class PostDestroyAPIView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostCreateAPIView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostCreateEditSerializer
