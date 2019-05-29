from django.contrib import admin
from .models import FeaturePost, FeatureComment

class FeatureDetails(admin.ModelAdmin):
    list_display = ('title', 'votes')
    
admin.site.register(FeaturePost, FeatureDetails)
admin.site.register(FeatureComment)
