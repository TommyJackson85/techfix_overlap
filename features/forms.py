from django import forms
from .models import Post


class FeaturePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'published_date')
