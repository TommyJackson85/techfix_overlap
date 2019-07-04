from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import time, datetime

STATUS_LABELS = [
    ('To Do', 'To Do'),
    ('Doing', 'Doing'), 
    ('Done', 'Done'),
]

class BugPost(models.Model):
    """
    A single Blog post
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

#start = models.IntegerField(default=0)
#end = models.DateTimeField(blank=True, null=True, default=timezone.now)
#1999-06-18 14:47:42
#2012-12-31 23:30 +0430
#datetime.datetime(1999, 12, 3, 14, 57, 11, 703055, tzinfo=<UTC>)
class BugComment(models.Model):
    """
    A single Blog comment
     on_delete=models.CASCADE,
    """
    post = models.ForeignKey(
        BugPost, related_name='bugs'
    )    
    user= models.ForeignKey(
       User, default=None, related_name='bugscommentuser'
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __unicode__(self):
        return self.content