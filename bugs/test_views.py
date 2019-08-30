from django.test import TestCase, Client
from .models import BugComment, BugPost
from .forms import BugPostForm, BugCommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

class TestViews(TestCase):

    def test_get_bug_posts(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugposts.html")
    
    def test_search_bug_posts(self):
        page = self.client.get("/bugs/search/?q=ggg")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugposts.html")
        
    def test_search_bug_posts_if_input_is_empty (self):
        page = self.client.get("/bugs/search/?q=")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugposts.html")

    def test_view_bug_post_detail (self):
        bug_post = BugPost(user_id=5, title="Create a Test", content="ggggg", views=0)
        bug_post.save()
        page = self.client.get("/bugs/{0}/".format(bug_post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugpostdetail.html")
       
    def test_comment_post_on_bug_post (self):
        
        #https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        bug_post = BugPost(user_id=user.pk, title="Create a Test", content="ggggg", views=0)
        bug_post.save()
        
        bug_comments = BugComment.objects.filter(post=bug_post).order_by('published_date')
    
        page = self.client.post("/bugs/{0}/".format(bug_post.id), {'content': 'testing'})
 
        bug_post.comment_count = bug_comments.count() 
        bug_post.save() 
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugpostdetail.html")
    
    def test_failed_view_of_nonexisting_bug_post_detail (self):
        page = self.client.get("/bugs/1/")
        self.assertEqual(page.status_code, 404)
    
   
    def test_get_edit_page_for_existing_bug_post_as_logged_in_user(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        bug_post = BugPost(user_id=user.pk, title="Create a Test", content="ggggg")
        bug_post.save()
        page = self.client.get("/bugs/{0}/edit/".format(bug_post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugpostform.html")
     
    
    def test_bug_post_edit_failure_as_logged_out_user(self):
        bug_post = BugPost(user_id=5, title="Create a Test", content="ggggg")
        bug_post.save()
        page = self.client.get("/bugs/{0}/edit/".format(bug_post.id))
  
        self.assertRedirects(page, '/accounts/login/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
     
    def test_bug_post_create_an_item(self):
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        bug_post = self.client.post("/bugs/new/", {"title": "Create a Test", "content": "ggggg"})

        self.assertEqual(bug_post.status_code, 302)
        self.assertRedirects(bug_post, '/bugs/1/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_get_edit_page_for_nonexisting_bug_post(self):
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        page = self.client.get("/bugs/1/edit/")
        self.assertEqual(page.status_code, 404)
  
    def test_deletion_of_existing_bug_post_if_it_belongs_to_user(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        bug_post = BugPost(id=4, user_id=user.pk, title="Create a Test", content="ggggg")
        bug_post.save()
        
        page = self.client.get("/bugs/{0}/delete/".format(bug_post.id))
        self.assertRedirects(page, "/bugs/", status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
  
    def test_bug_post_deletion_error_if_it_doesnt_belong_to_user(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        bug_post = BugPost(user_id=user.pk, title="Create a Test", content="ggggg")
        bug_post.save()
        
        page = self.client.get("/bugs/{0}/delete/".format(bug_post.id))
        self.assertRedirects(page, "/bugs/", status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
    
    def test_deletion_for_nonexisting_bug_post(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        page = self.client.get("/bugs/1/delete/")
        self.assertEqual(page.status_code, 404)

    def test_bug_post_deletion_failure_as_logged_out_user(self):
        
        page = self.client.get("/bugs/1/delete/")
        self.assertEqual(page.status_code, 302)
        
        self.assertRedirects(page, '/accounts/login/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_vote_bug_post(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        bug_post = BugPost(user_id=5, title="Create a Test", content="ggggg")
        bug_post.save()
        page = self.client.get("/bugs/{0}/vote/".format(bug_post.id))
        self.assertRedirects(page, '/bugs/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_bug_post_failure_as_logged_out_user(self):
            bug_post = BugPost(user_id=5, status="To Do", title="Create a Test", content="ggggg")
            bug_post.save()
            page = self.client.get("/bugs/{0}/vote/".format(bug_post.id))
            self.assertRedirects(page, '/accounts/login/', status_code=302, 
            target_status_code=200, fetch_redirect_response=True)
 
    def test_vote_bug_post_fail_none_found_bug(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        page = self.client.get("/bugs/1/vote/")
        self.assertEqual(page.status_code, 404)