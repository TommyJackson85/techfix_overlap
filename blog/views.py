from django.shortcuts import render
from .models import BlogPost
from django.utils import timezone

# Create your views here.
def get_blog_posts(request):
    user = request.user
    blog_posts = BlogPost.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    blog_count = 0
    for post in list(blog_posts):
        blog_count += 1
        
    print(blog_count)
    return render(request, "blogposts.html", {'blog_posts': blog_posts, 'blog_count': blog_count, 'user': user})
 