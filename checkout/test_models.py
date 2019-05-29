from django.contrib.auth.models import User
from django.test import TestCase
from .models import Order, OrderLineItem
from features.models import FeaturePost as FeatureVoted
from django.utils import timezone

# Create your tests here.
class TestCheckoutModels(TestCase):
    
    def test_Order_Model(self):
        current_date=timezone.now()
        order = Order(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address1="1 street_address", street_address2="2 street address", county="some county", date=current_date)
        order.save()
        self.assertEqual(order.full_name, "John Doe")
        self.assertEqual(order.phone_number, 123456789)
        self.assertEqual(order.country, "Ireland")
        self.assertEqual(order.postcode, "A12S34")
        self.assertEqual(order.town_or_city, "Some town")
        self.assertEqual(order.street_address1, "1 street_address")
        self.assertEqual(order.street_address2, "2 street address")
        self.assertEqual(order.county, "some county")
        
    def test_order_model_as_string(self):
        current_date=timezone.now()
        order = Order(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address1="1 street_address", street_address2="2 street address", county="some county", date=current_date)
        order.save()
        self.assertEqual(str(order.id)+"-"+str(order.date)+"-John Doe", str(order))
        
    def test_order_line_item_model(self):
        current_date=timezone.now()
        order = Order(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address1="1 street_address", street_address2="2 street address", county="some county", date=current_date)
        order.save()
        feature_voted = FeatureVoted(user=User.objects.create(username='Testuser'), title="new interactive form", content="list builder included in form", created_date="2019-05-24", published_date="2019-05-24", views=5, votes=5, votes_cost=52, status='To Do')
        feature_voted.save()
        orderlineitem = OrderLineItem(order=order,feature_voted=feature_voted,money_amount=23)
        orderlineitem.save()
        self.assertEqual(orderlineitem.order, order)
        self.assertEqual(orderlineitem.feature_voted, feature_voted)
        self.assertEqual(orderlineitem.money_amount, 23)
        self.assertEqual("23 @ new interactive form", str(orderlineitem))
        