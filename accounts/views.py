from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bugs.models import BugPost
from features.models import FeaturePost
from accounts.forms import UserLoginForm, UserRegistrationForm

def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect("/")

"""Return a login page"""
def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                #switched!
                auth.login(request, user)
                return redirect('profile')
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    logged_in_user_bugposts = BugPost.objects.filter(user=request.user)
    logged_in_user_featureposts = FeaturePost.objects.filter(user=request.user)
    return render(request, 'profile.html', {    "profile": user, 
                                                "bug_posts":logged_in_user_bugposts,
                                                "feature_posts":logged_in_user_featureposts
                                            }
    )
    
    
    
    