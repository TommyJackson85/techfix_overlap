from django.test import TestCase, Client
from django.shortcuts import render 
from .models import BlogPost 
from django.utils import timezone
from django.contrib.auth.models import User

class TestViews(TestCase):
    def test_get_blog_posts(self):
        """
        user = User.objects.create_user(
            username='Fake',
            email='Fake50@gggg.com',
            password='password1'
        )
        """
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogposts.html")