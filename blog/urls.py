from django.conf.urls import url
from .views import get_blog_posts

urlpatterns = [
    url(r'^$', get_blog_posts, name='get_blog_posts'),
]