from django.db import models
from django.conf import settings
from blog.models import BlogPost


User = settings.AUTH_USER_MODEL

# Create your models here.
class Comment(models.Model):
  user =models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
  post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
