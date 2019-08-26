from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time, datetime

"""" used  for toggling post statuses """
STATUS_LABELS = [
    ('To Do', 'To Do'),
    ('Doing', 'Doing'), 
    ('Done', 'Done'),
]

class BugPost(models.Model):
    """
    A single Bug post
    """
    user= models.ForeignKey(
       User, default=None, on_delete=models.CASCADE, related_name='bugs'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_LABELS, default='To Do')
    comment_count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title


class BugComment(models.Model):
    """
    A single Bug comment
    """
    post = models.ForeignKey(
        BugPost, on_delete=models.CASCADE, related_name='bugs'
    )    
    user= models.ForeignKey(
       User, default=None, on_delete=models.CASCADE, related_name='bugscommentuser'
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __unicode__(self):
        return self.content