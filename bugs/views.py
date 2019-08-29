from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from .models import BugPost, BugComment
from .forms import BugPostForm, BugCommentForm

def vote_bug_post(request, pk):
    """
    Upvotes bug post redirects to list of bug posts
    """
    if not request.user.is_authenticated:
        messages.error(request, "Please login before voting for bug reports!")
        return redirect('/accounts/login/')
    
    bug_post = get_object_or_404(BugPost, pk=pk)
    
    if bug_post.status == "Done":
        messages.error(request, "Voting not allowed because this bug report has been finsihed!")
        return redirect("/bugs/{0}/".format(bug_post.id))
    
    bug_post.votes += 1
    bug_post.save()
    bug_posts = BugPost.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    messages.success(request, "You have successfully voted for the bug report and have been directed to the listings!")
    return redirect(get_bug_posts)

def get_bug_posts(request):
    """
    Create a view that will return a list
    of Bug Posts that were published prior to 'now'
    and render them to the 'bugposts.html' template
    """
    user = request.user
    bug_posts = BugPost.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    
    doing_count=0
    to_do_count=0
    done_count=0
    
    for post in list(bug_posts):
        if post.status == 'Doing':
            doing_count += 1
        if post.status == 'To Do':
            to_do_count += 1
        if post.status == 'Done':
            done_count += 1
    
    return render(request, "bugposts.html", {'bug_posts': bug_posts, 'doing_count': doing_count, 'to_do_count': to_do_count, 'done_count': done_count, 'user': user})
    
    
def search_bug_posts(request):
    """
    Create a view that will return a list
    of Bug Posts that were published prior to 'now'
    and render them to the 'bugposts.html' template
    """
    user = request.user
    bug_posts = BugPost.objects.filter(title__icontains=request.GET['q'], published_date__lte=timezone.now())
    doing_count = 0
    to_do_count = 0
    done_count = 0
    for post in list(bug_posts):
        if post.status == 'Doing':
            doing_count += 1
        if post.status == 'To Do':
            to_do_count += 1
        if post.status == 'Done':
            done_count += 1
    messages.success(request, "Search results can be seen below!")
    return render(request, "bugposts.html", {'bug_posts': bug_posts, 'doing_count': doing_count, 'to_do_count': to_do_count, 'done_count': done_count, 'user': user})

def bug_post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'bugpostdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    bug_post = get_object_or_404(BugPost, pk=pk) if pk else None
    bug_post.views += 1
    bug_post.save()
    
    """
    Used this stack overflow post for reference in building comment functions.
    https://stackoverflow.com/questions/43421904/how-to-link-a-comment-to-a-single-post-in-django
    """   
    bug_comments = BugComment.objects.filter(post=bug_post).order_by('published_date')
    
    if request.method == 'POST':
        
        if not request.user.is_authenticated:
            messages.error(request, "Please login first before posting comments!")
            return redirect('login')
            
        
        form = BugCommentForm(request.POST)
        
        if bug_post is not None:
            if request.user != bug_post.user:
                if bug_post.status == "Doing":
                    messages.error(request, "Commenting not allowed because this bug report has been finsihed!")
                messages.error(request, "You cannot post comments on another users bug report!")
                return redirect(bug_post_detail, bug_post.pk)
        
        if bug_post.status == "Done":
            messages.error(request, "Commenting not allowed because this bug report has been finsihed!")
            return render(request, "bugpostdetail.html", {'bug_post': bug_post, 'form': form, 'bug_comments': bug_comments})
    
    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = bug_post
            comment.user = request.user
            comment.save()
            
            bug_post.comment_count = bug_comments.count()
            bug_post.save()
            form = BugCommentForm()
            messages.success(request, "You have successfully commented on this bug report!")
    else:
        form = BugCommentForm()
        
    return render(request, "bugpostdetail.html", {'bug_post': bug_post, 'form': form, 'bug_comments': bug_comments})

def create_or_edit_bugpost(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    
    if not request.user.is_authenticated:
        messages.error(request, "Please login first before posting or editing bug reports!")
        return redirect('login')
    
    bug_post = get_object_or_404(BugPost, pk=pk) if pk else None
    
    if bug_post is not None:
        if request.user != bug_post.user:
            if bug_post.status != "To Do":
                messages.error(request, "Editing not allowed because this bug report has been finsihed or is in progress!")
            messages.error(request, "You cannot edit another users bug!")
            return redirect(bug_post_detail, bug_post.pk)
    
        try:         
            if bug_post.status != "To Do":
                messages.error(request, "Editing not allowed because this bug report has been finsihed or is in progress!")
                return redirect("/bugs/{0}/".format(bug_post.id))
        except AttributeError:
            #catches errors with making new post
            pass
        
    if request.method == "POST":
        
        if not request.user.is_authenticated:
            messages.error(request, "Please login first before posting or editing bug reports!")
            return redirect('login')
    
        if bug_post is not None:
            if request.user != bug_post.user:
                if bug_post.status != "To Do":
                    messages.error(request, "Editing is not allowed because this bug report has been finsihed or is in progress!")
                messages.error(request, "You cannot edit another users bug!")
                return redirect(bug_post_detail, bug_post.pk)
                
        try:        
            if bug_post.status != "To Do":
                messages.error(request, "Editing not allowed because this bug report has been finsihed or is in progress!")
                return redirect("/bugs/{0}/".format(bug_post.id))
        except AttributeError:
            pass
            

        #receive form
        form = BugPostForm(request.POST, request.FILES, instance=bug_post)
        #receive user name
        #form.username = user
        if form.is_valid():
            bug_post = form.save(commit=False)
            bug_post.user = request.user
            bug_post = form.save()

            print("My Time")

            messages.success(request, "You have successfully created / edited this bug report!")
            return redirect(bug_post_detail, bug_post.pk)
    else:
        form = BugPostForm(instance=bug_post)
    return render(request, 'bugpostform.html', {'form': form, 'bug_post': bug_post})
    
def delete_bug_post(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    
    if not request.user.is_authenticated:
        messages.error(request, "Please login first before deleting bug reports!")
        return redirect('login')
    
    post = get_object_or_404(BugPost, pk=pk)
        
    if request.user != post.user:
        if post.status != "To Do":
            messages.error(request, "Deleting not allowed because this bug report has been finsihed or is in progress!")
        messages.error(request, "You cannot delete another users bug report!")
        return redirect(bug_post_detail, post.pk)
    
    if post.status != "To Do":
        messages.error(request, "Deleting not allowed because this bug report has been finsihed or is in progress!")
        return redirect("/bugs/{0}/".format(post.id))
    
    post.delete()
    messages.success(request, "You have successfully deleted the bug report and have been directed to the listings!")
    return redirect(get_bug_posts)
 