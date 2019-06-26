from django.conf.urls import url
from .views import get_charts

urlpatterns = [
    url(r'^$', get_charts, name='get_charts'),
    #url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    #url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]