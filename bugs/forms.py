from django import forms
from .models import BugPost, BugComment


class BugPostForm(forms.ModelForm):
    
    class Meta:
        model = BugPost
        fields = ('title', 'content')


class BugCommentForm(forms.ModelForm):
    
    class Meta:
        model = BugComment
        fields = ('content',)
