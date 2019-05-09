from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import FeaturePostForm


def get_feature_posts(request):
    """
    Create a view that will return a list
    of Feature Posts that were published prior to 'now'
    and render them to the 'featureposts.html' template
    """
    feature_posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "featureposts.html", {'feature_posts': feature_posts})


def feature_post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'featurepostdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    feature_post = get_object_or_404(Post, pk=pk)
    feature_post.views += 1
    feature_post.save()
    return render(request, "featurepostdetail.html", {'feature_post': feature_post})


def create_or_edit_featurepost(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    feature_post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = FeaturePostForm(request.POST, request.FILES, instance=feature_post)
        if form.is_valid():
            feature_post = form.save()
            return redirect(feature_post_detail, feature_post.pk)
    else:
        form = FeaturePostForm(instance=feature_post)
    return render(request, 'featurepostform.html', {'form': form})
