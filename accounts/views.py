from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bugs.models import BugPost
from features.models import FeaturePost
from blog.models import BlogPost
from accounts.forms import UserLoginForm, UserRegistrationForm

def index(request):
    """Return the index.html file"""
    bug_posts = BugPost.objects.order_by('-published_date')[:5]
    feature_posts = FeaturePost.objects.order_by('-published_date')[:5]
    blog_posts = BlogPost.objects.order_by('-published_date')[:5]
    return render(request, 'index.html', {'bug_posts': bug_posts, 'feature_posts': feature_posts, 'blog_posts': blog_posts})

@login_required
def logout(request):
        
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect("/")

"""Return a login page"""
def login(request):
    
    if request.user.is_authenticated:
        messages.error(request, "Please logout of current account first!")
        return redirect(index)
        
    if request.method == "POST":
        
        login_form = UserLoginForm(request.POST)
        
        if request.user.is_authenticated:
            messages.error(request, "Please logout of current account first!")
            return redirect(index)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                #switched!
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('profile')
            else:
                messages.error(request, "Your username or password is incorrect!")
                
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    
    if request.user.is_authenticated:
        messages.error(request, "Please logout of current account first!")
        return redirect(index)
    
    if request.method == "POST":
        
        if request.user.is_authenticated:
            messages.error(request, "Please logout of current account first!")
            return redirect(index)
        
        registration_form = UserRegistrationForm(request.POST)
        
        
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered and are now logged in!")
                return redirect('profile')
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    
    if not request.user.is_authenticated:
        messages.error(request, "Please login first!")
        return redirect('login')
    
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    logged_in_user_bugposts = BugPost.objects.filter(user=request.user)
    logged_in_user_featureposts = FeaturePost.objects.filter(user=request.user)
    
    bug_count = 0
    for bug in list(logged_in_user_bugposts):
        bug_count += 1
        
    feature_count = 0
    for feature in list(logged_in_user_featureposts):
        feature_count += 1
    
    
    return render(request, 'profile.html', {    "profile": user, 
                                                "bug_posts":logged_in_user_bugposts,
                                                "feature_posts":logged_in_user_featureposts,
                                                "bug_count": bug_count,
                                                "feature_count": feature_count,
                                            }
    )
    
    
    
    