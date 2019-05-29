from django import forms
from .models import FeaturePost, FeatureComment


class FeaturePostForm(forms.ModelForm):
    
    class Meta:
        model = FeaturePost
        fields = ('title', 'content', 'published_date')
        

class FeatureCommentForm(forms.ModelForm):
    
    class Meta:
        model = FeatureComment
        fields = ('content', 'published_date')
