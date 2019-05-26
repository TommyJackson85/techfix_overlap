from django.test import TestCase
from .models import Post

# Create your tests here.

class PostTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """
    def test_str(self):
        #user field from model
        test_content = Post(title='Test Bug Post', content="This bus being tested", views=0, votes=0)
        self.assertEqual(test_content.title, 'Test Bug Post')
        self.assertEqual(test_content.content, "This bus being tested")
        self.assertEqual(test_content.views, 0)
        self.assertEqual(test_content.votes, 0)
