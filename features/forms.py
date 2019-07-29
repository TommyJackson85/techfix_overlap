from django import forms
from .models import FeaturePost, FeatureComment


class FeaturePostForm(forms.ModelForm):
    
    class Meta:
        model = FeaturePost
        fields = ('title', 'content')
        

class FeatureCommentForm(forms.ModelForm):
    
    class Meta:
        model = FeatureComment
        fields = ('content',)
