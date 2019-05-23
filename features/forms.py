from django import forms
from .models import Post, Comment


class FeaturePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'published_date')
        

class FeatureCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content', 'published_date')
