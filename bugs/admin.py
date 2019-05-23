from django.contrib import admin
from .models import Post, Comment


class PostDetails(admin.ModelAdmin):
    list_display = ('title', 'votes')
admin.site.register(Post, PostDetails)

admin.site.register(Comment)



