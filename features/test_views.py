from django.test import TestCase, Client
from .models import FeatureComment, FeaturePost
from .forms import FeaturePostForm, FeatureCommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

class TestViews(TestCase):

    def test_get_feature_posts(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureposts.html")
    
    def test_search_feature_posts(self):
        page = self.client.get("/features/search/?q=ggg")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureposts.html")
        
    def test_search_feature_posts_if_input_is_empty (self):
        page = self.client.get("/features/search/?q=")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureposts.html")

    def test_view_feature_post_detail (self):
        feature_post = FeaturePost(user_id=5, title="Create a Test", content="ggggg", views=0)
        feature_post.save()
        page = self.client.get("/features/{0}/".format(feature_post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featurepostdetail.html")
       
    def test_comment_post_on_feature_post(self):
        #https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        feature_post = FeaturePost(user_id=5, title="Create a Test", content="ggggg", views=0)
        feature_post.save()
        
        feature_comments = FeatureComment.objects.filter(post=feature_post).order_by('published_date')
    
        page = self.client.post("/features/{0}/".format(feature_post.id), {'content': 'testing'})
 
        feature_post.comment_count = feature_comments.count() 
        feature_post.save() 
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featurepostdetail.html")
    
    def test_failed_view_of_nonexisting_feature_post_detail (self):
        page = self.client.get("/features/1/")
        self.assertEqual(page.status_code, 404)
        

    def test_edit_existing_feature_failuere_as_logged_out_user(self):
        
        feature_post = FeaturePost(user_id=5, title="Create a Test", content="ggggg")
        feature_post.save()
        page = self.client.get("/features/{0}/edit/".format(feature_post.id))
        self.assertRedirects(page, '/accounts/login/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    """    
    def test_get_edit_page_for_existing_feature_post_as_logged_in_user(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        feature_post = FeaturePost(user_id=5, title="Create a Test", content="ggggg")
        feature_post.save()
        page = self.client.get("/features/{0}/edit/".format(feature_post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featurepostform.html")
    """  
    def test_feature_post_create_an_item(self):
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        feature_post = self.client.post("/features/new/", {"title": "Create a Test", "content": "ggggg"})

        self.assertEqual(feature_post.status_code, 302)
        self.assertRedirects(feature_post, '/features/1/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_get_edit_page_for_nonexisting_feature_post(self):
        
        user = User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        page = self.client.get("/features/1/edit/")
        self.assertEqual(page.status_code, 404)
