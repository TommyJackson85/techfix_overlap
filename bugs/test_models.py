from django.test import TestCase
from django.contrib.auth.models import User
from .models import BugPost, BugComment
from .forms import BugPostForm, BugCommentForm
from django.utils import timezone
import datetime

# Create your tests here.

class BugPostTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """
    
    def test_can_create_a_bug_post(self):
        #user field from model
        User.objects.create(username="Tom50")
        test_bug_post = BugPost(user=User.objects.create_user('test_user', None, 'qwertxxx123'), title='Test Bug Post', content="This bus being tested", created_date=datetime.date(2018, 12, 25), published_date=datetime.date(2018, 12, 25))
        self.assertEqual(test_bug_post.user.username, 'test_user')
        self.assertEqual(test_bug_post.title, 'Test Bug Post')
        self.assertEqual(test_bug_post.content, "This bus being tested")
        self.assertEqual(test_bug_post.created_date, datetime.date(2018, 12, 25))
   
        self.assertEqual(test_bug_post.published_date, datetime.date(2018, 12, 25)) 
        self.assertEqual(test_bug_post.views, 0)
        self.assertEqual(test_bug_post.votes, 0)
        self.assertEqual(test_bug_post.status, "To Do")
        self.assertEqual(test_bug_post.comment_count, 0)
    
    
    def test_can_create_a_bug_comment_and_increment_bug_post_comment_count(self):
        test_bug_post = BugPost(user=User(username="Tom50"), title='Test Bug Post', content="This bus being tested", created_date=timezone.now(), published_date=timezone.now())
        test_bug_comment = BugComment(user=User(username="Tom50"), post=test_bug_post, content="This reply is being tested", created_date=timezone.now(), published_date=timezone.now())
        test_bug_post.comment_count += 1
        self.assertEqual(test_bug_post.comment_count, 1)
        
    def test_can_increment_votes_and_views_of_bug_post(self):
        test_bug_post = BugPost(user=User(username="Tom50"), title='Test Bug Post', content="This bus being tested", created_date=timezone.now(), published_date=timezone.now())
        test_bug_post.votes += 1
        test_bug_post.views += 1
        test_bug_post.views += 1
        
        self.assertEqual(test_bug_post.votes, 1)
        self.assertEqual(test_bug_post.views, 2)
        
        def can_change_bug_post_status_to_Not_Doing(self):
            test_bug_post = BugPost(user=User(username="Tom50"), title='Test Bug Post', content="This bus being tested", created_date=timezone.now(), published_date=timezone.now())
            test_bug_post.status = "Doing"
           
            self.assertEqual(test_bug_post.status, "Doing")
        
    """
        post = models.ForeignKey(
        BugPost, related_name='bugs'
    )    
    user= models.ForeignKey(
       User, default=None, on_delete=models.CASCADE, related_name='bugscommentuser'
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    """
       
    """
        class BugCommentTests(TestCase):
            def test_can_create_a_bug_comment(self):
    
    
        class BugPostFormTest(TestCase):
            def test_str(self):
                test_content = BugPostForm()
     
        class TestItemModel(TestCase):
        
            def test_done_defaults_to_False(self):
                item = Item(name="Create a Test")
                item.save()
                self.assertEqual(item.name, "Create a Test")
                self.assertFalse(item.done)
            
            def test_can_create_an_item_with_a_name_and_status(self):
                item = Item(name="Create a Test", done=True)
                item.save()
                self.assertEqual(item.name, "Create a Test")
                self.assertTrue(item.done)
    """