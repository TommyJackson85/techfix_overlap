from django.test import TestCase
from features.models import FeaturePost as FeatureVoted
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

    def test_add_cart(self):
        cart = [{"feature_voted": {"title": "ddd"},
                "product": {"description": "dddd", "price": 500 }
        }]
        page = self.client.get("/cart/add/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
    def test_get_404_on_add_to_cart_item_with_no_feature_id(self):
        #Change URL
        response = self.client.get("/cart/add")
        self.assertEqual(response.status_code, 404)