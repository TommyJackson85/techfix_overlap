from django.contrib import admin
from .models import BlogPost

class BlogDetails(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    
admin.site.register(BlogPost, BlogDetails)

# Register your models here.
