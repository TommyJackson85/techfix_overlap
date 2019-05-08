from django.conf.urls import url
from .views import get_bug_posts, bug_post_detail, create_or_edit_bugpost

urlpatterns = [
    url(r'^$', get_bug_posts, name='get_bug_posts'),
    url(r'^(?P<pk>\d+)/$', bug_post_detail, name='bug_post_detail'),
    url(r'^new/$', create_or_edit_bugpost, name='new_bug_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bugpost, name='edit_bug_post')
]