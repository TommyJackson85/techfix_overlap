from django.conf.urls import url
from .views import get_bug_posts, search_bug_posts, bug_post_detail, create_or_edit_bugpost, vote_bug_post, delete_bug_post
# ?q=
urlpatterns = [
    url(r'^$', get_bug_posts, name='get_bug_posts'),
    url(r'^search/$', search_bug_posts, name='search_bug_posts'),
    url(r'^(?P<pk>\d+)/vote/$', vote_bug_post, name='vote_bug_post'),
    url(r'^(?P<pk>\d+)/delete/$', delete_bug_post, name='delete_bug_post'),
    url(r'^(?P<pk>\d+)/$', bug_post_detail, name='bug_post_detail'),
    url(r'^new/$', create_or_edit_bugpost, name='new_bug_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bugpost, name='edit_bug_post'),
]