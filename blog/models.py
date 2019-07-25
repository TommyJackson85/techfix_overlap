from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time, datetime

class BlogPost(models.Model):
    """
    A single Blog post
    """
    user= models.ForeignKey(
       User, default=None, on_delete=models.CASCADE, related_name='blog'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    def __unicode__(self):
        return self.title