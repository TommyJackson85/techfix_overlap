from django.contrib import admin
from .models import BugPost, BugComment


class PostDetails(admin.ModelAdmin):
    list_display = ('title', 'votes')
admin.site.register(BugPost, PostDetails)

admin.site.register(BugComment)



