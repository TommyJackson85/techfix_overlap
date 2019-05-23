from django.contrib import admin
from .models import Post, Comment

class FeatureDetails(admin.ModelAdmin):
    list_display = ('title', 'votes')
    
admin.site.register(Post, FeatureDetails)
admin.site.register(Comment)
