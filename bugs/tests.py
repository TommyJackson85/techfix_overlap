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
        test_content = Post(title='Gerry owe!!')
        self.assertEqual(str(test_content), 'Gerry owe!!')
