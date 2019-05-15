from django.conf.urls import url
from .views import get_feature_posts, feature_post_detail, create_or_edit_featurepost, vote_feature_post

urlpatterns = [
    url(r'^$', get_feature_posts, name='get_feature_posts'),
    url(r'^(?P<pk>\d+)/vote/$', vote_feature_post, name='vote_feature_post'),
    url(r'^(?P<pk>\d+)/$', feature_post_detail, name='feature_post_detail'),
    url(r'^new/$', create_or_edit_featurepost, name='new_feature_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_featurepost, name='edit_feature_post')
]