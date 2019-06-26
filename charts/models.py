"""
from bugs.models import BugPost
from django.db import models

# Create your models here.
class BugPostProgressTime(models.Model):
    bug_post = models.ForeignKey(
       BugPost, default=None, on_delete=models.CASCADE, related_name='bugs'
    )
    start_date = models.DateField((u"Start Date"), blank=True)
    start_time = models.TimeField((u"Start Time"), blank=True)
        
    def __unicode__(self):
        return self.content
"""