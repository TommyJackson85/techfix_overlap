from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from .forms import BugPostForm

def vote_bug_post(request, pk):
    """
    Upvotes bug post redirects to list of bug posts
    """
    bug_post = get_object_or_404(Post, pk=pk)
    bug_post.votes += 1
    bug_post.save()
    bug_posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return redirect(get_bug_posts)

    

def get_bug_posts(request):
    """
    Create a view that will return a list
    of Bug Posts that were published prior to 'now'
    and render them to the 'bugposts.html' template
    """
    user = request.user
    bug_posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "bugposts.html", {'bug_posts': bug_posts, 'user': user})


def bug_post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'bugpostdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    bug_post = get_object_or_404(Post, pk=pk)
    bug_post.views += 1
    bug_post.save()
    return render(request, "bugpostdetail.html", {'bug_post': bug_post})


def create_or_edit_bugpost(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    bug_post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        #receive form
        form = BugPostForm(request.POST, request.FILES, instance=bug_post)
        #receive user name
        #form.username = user
        if form.is_valid():
            bug_post = form.save(commit=False)
            bug_post.user = request.user
            bug_post = form.save()
            return redirect(bug_post_detail, bug_post.pk)
    else:
        form = BugPostForm(instance=bug_post)
    return render(request, 'bugpostform.html', {'form': form})