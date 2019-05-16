from django import forms
from .models import Post, Comment


class BugPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'published_date')


class BugCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content', 'published_date')
