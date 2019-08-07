from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import FeaturePost, FeatureComment
from .forms import FeaturePostForm, FeatureCommentForm

def get_feature_posts(request):
    """
    Create a view that will return a list
    of Bug Posts that were published prior to 'now'
    and render them to the 'bugposts.html' template
    """
    user = request.user
    feature_posts = FeaturePost.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    
    doing_count=0
    to_do_count=0
    done_count=0
    
    for post in list(feature_posts):
        if post.status == 'Doing':
            doing_count += 1
        if post.status == 'To Do':
            to_do_count += 1
        if post.status == 'Done':
            done_count += 1
    
    return render(request, "featureposts.html", {'feature_posts': feature_posts, 'doing_count': doing_count, 'to_do_count': to_do_count, 'done_count': done_count, 'user': user})
   



def search_feature_posts(request):
    """
    Create a view that will return a list
    of Bug Posts that were published prior to 'now'
    and render them to the 'bugposts.html' template
    """
    user = request.user
    feature_posts = FeaturePost.objects.filter(title__icontains=request.GET['q'], published_date__lte=timezone.now())
    doing_count = 0
    to_do_count = 0
    done_count = 0
    for post in list(feature_posts):
        if post.status == 'Doing':
            doing_count += 1
        if post.status == 'To Do':
            to_do_count += 1
        if post.status == 'Done':
            done_count += 1
    messages.success(request, "Search results can be seen below!")
    return render(request, "featureposts.html", {'feature_posts': feature_posts, 'doing_count': doing_count, 'to_do_count': to_do_count, 'done_count': done_count, 'user': user})



def feature_post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'featurepostdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    
    feature_post = get_object_or_404(FeaturePost, pk=pk) if pk else None
    feature_post.views += 1
    feature_post.save()
    
    """
    Used this stack overflow post for reference in building comment functions.
    https://stackoverflow.com/questions/43421904/how-to-link-a-comment-to-a-single-post-in-django
    """   
    feature_comments = FeatureComment.objects.filter(post=feature_post).order_by('published_date')
    
    if request.method == 'POST':
        form = FeatureCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= feature_post
            comment.user = request.user
            comment.save()
            feature_post.comment_count = feature_comments.count()
            feature_post.save()
            messages.success(request, "You have successfully commented on this feature request!")
            
    else:
        form = FeatureCommentForm()
    return render(request, "featurepostdetail.html", {'feature_post': feature_post, 'form': form, 'feature_comments': feature_comments})


def create_or_edit_featurepost(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    feature_post = get_object_or_404(FeaturePost, pk=pk) if pk else None
    if request.method == "POST":
        form = FeaturePostForm(request.POST, request.FILES, instance=feature_post)
        if form.is_valid():
            feature_post = form.save(commit=False)
            feature_post.user = request.user
            feature_post = form.save()
            
            messages.success(request, "You have successfully created / edited this feature request!")
            return redirect(feature_post_detail, feature_post.pk)
    else:
        form = FeaturePostForm(instance=feature_post)
    return render(request, 'featurepostform.html', {'form': form, 'feature_post': feature_post})

