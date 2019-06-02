from django import forms
from .models import BugPost, BugComment
from django.test import TestCase
from .forms import BugPostForm, BugCommentForm

class TestToDoItemForm(TestCase):

    def test_can_not_create_bug_post_with_just_a_title(self):
        form = BugPostForm({'title': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_can_not_create_bug_post_with_just_a_comment(self):
        form = BugPostForm({'comment': 'Create Tests'})
        self.assertFalse(form.is_valid())   
    
    def can_create_bug_post_from_form(self):
        form = BugPostForm({'title': 'newbug', 'content': 'the new bug is dangerous'})
        self.assertTrue(form.is_valid())
        
    def test_can_not_create_comment_post_with_just_empty_comment(self):
        form = BugCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())  
        
    def can_create_comment_post_from_form(self):
        form = BugCommentForm({'content': 'I am commenting on this bug post', 'published_date': '2019-05-29'})
        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_missing_title(self):
        form = BugPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
    def test_correct_message_for_missing_post_content(self):
        form = BugPostForm({'title': 'this was done.'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
        
    def test_correct_message_for_missing_comment_content(self):
        form = BugCommentForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
        
    def test_correct_message_for_missing_name(self):
        form = BugPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])