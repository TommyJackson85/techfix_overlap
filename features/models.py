from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

"""" used  for toggling post statuses """
STATUS_LABELS = [
    ('To Do', 'To Do'),
    ('Doing', 'Doing'), 
    ('Done', 'Done'),
]

class FeaturePost(models.Model):
    """
    A single Feature post
    """
    user= models.ForeignKey(
       User, default=None, on_delete=models.CASCADE, related_name='features'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    votes_cost = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_LABELS, default='To Do')
    comment_count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title

        
class FeatureComment(models.Model):
    """
    A single Feature comment
    """
    post = models.ForeignKey(
        FeaturePost, on_delete=models.CASCADE, related_name='features'
    )    
    user= models.ForeignKey(
       User, default=None, on_delete=models.CASCADE, related_name='featurescommentuser'
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __unicode__(self):
        return self.content