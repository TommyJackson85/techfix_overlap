from django.test import TestCase
from features.models import FeaturePost as FeatureVoted
from django.contrib.auth.models import User
#from .context import cart_contents
from decimal import Decimal
# Create your tests here.
class TestCartViews(TestCase):
    
    def test_view_cart(self):
        """
        cart_items = [{"feature_voted": {"title": "ddd"},
                    "product": {"description": "dddd", "price": 500 }
        }]
        """
        
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
    def test_get_404_on_adjust_cart_item_with_no_feature_id(self):
        #Change URL
        response = self.client.get("/cart/adjust")
        
        self.assertEqual(response.status_code, 404)

    def test_add_item_to_cart(self):
        #https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        feature_voted = FeatureVoted(user_id=5, title="Create a Test", content="ggggg")
        feature_voted.save()
        total_cost = 0
        money_amount = 20
        
        self.assertEqual(feature_voted.id, 1)
        cart = {}
        cart[feature_voted.id] = cart.get(feature_voted.id, money_amount)
        
        session['cart'] = cart
        session.save()

        page_1 = self.client.get("/cart/add/{0}".format(feature_voted.id))
        self.assertEqual(cart, {1: 20})
        self.assertRedirects(page_1, '/cart/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    def test_adjust_cart_item_then_remove(self):  
        #testing forms
        #https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        session = self.client.session
        
        feature_voted = FeatureVoted(user_id=5, title="Create a Test", content="ggggg")
        feature_voted.save()
        
        total_cost = 20
        
        quantity = 4
        
        self.assertEqual(feature_voted.id, 1)
        cart = {}
        cart[feature_voted.id] = quantity

        page_2 = self.client.post("/cart/adjust/{0}".format(feature_voted.id), {'quantity':quantity})
        
        self.assertRedirects(page_2, '/cart/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        #quantity to 0 will remove item
        page_3 = self.client.post("/cart/adjust/{0}".format(feature_voted.id), {'quantity':0})
        
        self.assertRedirects(page_3, '/cart/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_get_404_on_add_to_cart_item_with_no_feature_id(self):
        #Change URL
        response = self.client.get("/cart/add")
        self.assertEqual(response.status_code, 404)