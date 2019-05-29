from django import forms
from .models import BugPost, BugComment
from django.test import TestCase
from .forms import BugPostForm, BugCommentForm

class TestToDoItemForm(TestCase):
    def can_create_bug_post_from_form(self):
        form = BugPostForm({'title': 'newbug', 'content': 'the new bug is dangerous', 'published_date': '2019-05-27'})
        self.assertTrue(form.is_valid())
        
    def can_create_comment_post_from_form(self):
        form = BugCommentForm({'content': 'I am commenting on this bug post', 'published_date': '2019-05-29'})
        self.assertTrue(form.is_valid())