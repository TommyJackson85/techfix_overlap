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

    def test_failed_view_of_nonexisting_bug_post_detail (self):
        page = self.client.get("/bugs/1/")
        self.assertEqual(page.status_code, 404)
        
    def test_get_edit_page_for_existing_bug_post(self):
        bug_post = BugPost(user_id=5, title="Create a Test", content="ggggg")
        bug_post.save()
        page = self.client.get("/bugs/{0}/edit/".format(bug_post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugpostform.html")
        
    def test_post_create_an_item(self):
        user = User.objects.create_user(username='Ems_1', password='generic')
        response = self.client.post("/bugs/new/", {"title": "Create a Test", "content": "ggggg"})
        bug_post = get_object_or_404(BugPost, pk=1)
        bug_post.user = User.objects.create_user(username='Ems_1', password='generic')
        bug_post.save()
        self.assertEqual(bug_post.user, 'test_user')
        
    def test_get_edit_page_for_nonexisting_bug_post(self):
        page = self.client.get("/bugs/1/edit/")
        self.assertEqual(page.status_code, 404)
        
    def test_deletion_of_existing_bug_post(self):
        bug_post = BugPost(user_id=5, title="Create a Test", content="ggggg")
        bug_post.save()
        page = self.client.get("/bugs/{0}/delete/".format(bug_post.id))
        self.assertRedirects(page, '/bugs/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_deletion_for_nonexisting_bug_post(self):
        page = self.client.get("/bugs/1/delete/")
        self.assertEqual(page.status_code, 404)

    def test_vote_bug_post(self):
        bug_post = BugPost(user_id=5, title="Create a Test", content="ggggg")
        bug_post.save()
        page = self.client.get("/bugs/{0}/vote/".format(bug_post.id))
        self.assertRedirects(page, '/bugs/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_vote_bug_post_fail(self):
        page = self.client.get("/bugs/1/vote/")
        self.assertEqual(page.status_code, 404)
        

        
    """
    def vote_bug_post(request, pk):
        
        Upvotes bug post redirects to list of bug posts
        
        bug_post = get_object_or_404(BugPost, pk=pk)
        bug_post.votes += 1
        bug_post.save()
        bug_posts = BugPost.objects.filter(published_date__lte=timezone.now()
            ).order_by('-published_date')
        return redirect(get_bug_posts)
       
     
    def test_get_bug_posts(self):
        page = self.client.get("/bugs/search/?q=")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugposts.html")
    """
    
    
    
    """
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_item_page(self):
        item = Item(name="Create a Test")
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
    """    