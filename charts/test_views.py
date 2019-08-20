from django.test import TestCase, Client
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from bugs.models import BugPost
from features.models import FeaturePost
from .views import chunks, get_most_voted, get_averages

import pprint, json

import time, datetime

class TestViews(TestCase):
    def test_get_charts_with_no_data(self):
        #no bugs or features found
        page = self.client.get("/charts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "charts.html")

    def test_get_charts_with_bug_posts_data(self):
        now = datetime.datetime(2019, 8, 13, 13, 11, 22, 50)
        #now example is a fake instance of timeóne.now()
        user = User.objects.create_user(
            username='Fake',
            email='Fake50@gggg.com',
            password='password1'
        )
        three_months_past = datetime.date.today() - datetime.timedelta(3*365/12)
        all_days = []
        d = three_months_past
        
        while d <=  datetime.date.today():
            all_days.append(d) 
            d += datetime.timedelta(days=1) 
        
        bug_posts = [
            BugPost(user_id=5, title="Create a Test", content="ggggg", start_time=datetime.datetime(2019, 6, 25, 19, 52, 5, 58), end_time=datetime.datetime(2018, 7, 25, 19, 52, 58), votes=5), 
            BugPost(user_id=6, title="Something", content="etc...", start_time=datetime.datetime(2018, 5, 24, 19, 52, 28, 58), end_time=datetime.datetime(2018, 8, 1, 19, 52, 28, 58), votes=2),
            BugPost(user_id=6, title="Something", content="etc...", start_time=datetime.datetime(2018, 5, 24, 19, 52, 28), end_time=None, votes=10)
        ]
        
        bug_post_averages = get_averages(bug_posts, now, all_days, user)
        most_voted_bugs = get_most_voted(bug_posts)
        # BugPost.objects.filter(Q(start_time__gte=three_months_past) | Q(end_time__gte=three_months_past)) 
        feature_posts_time = [ FeaturePost(user_id=5, title="Create a Test", content="ggggg"), FeaturePost(user_id=6, title="Something", content="etc...")]
        
        page = self.client.get("/charts/")
        self.assertEqual(now, datetime.datetime(2019, 8, 13, 13, 11, 22, 50))
        self.assertEqual(bug_posts[1].start_time, datetime.datetime(2018, 5, 24, 19, 52, 28, 58))
        self.assertEqual(len(bug_posts), 3)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "charts.html")