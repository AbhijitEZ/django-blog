from django.urls import path, include
from .views import PostListAPIView, PostDetailAPIView, PostDestroyAPIView, PostEditAPIView, PostCreateAPIView


app_name = 'api-posts'


urlpatterns = [
    path('', PostListAPIView.as_view(), name="list-api"),
    path('detail/<slug>/', PostDetailAPIView.as_view(), name="detail-api"),
    path('create/', PostCreateAPIView.as_view(), name="create-api"),
    path('delete/<slug>/', PostDestroyAPIView.as_view(), name="delete-api"),
    path('edit/<slug>/', PostEditAPIView.as_view(), name="edit-api"),
]
