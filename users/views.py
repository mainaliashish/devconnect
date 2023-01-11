from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages

from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = { 'profiles': profiles }
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = { 'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills }
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    # user = request.user
    profile = request.user.profile
    topSkills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'topSkills': topSkills, 'projects': projects}
    return render(request, 'users/account.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or password is incorrect.")

    return render(request, 'users/login_register.html')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account created successfully.")

            login(request, user)
            return redirect('profiles')
        else:
            messages.success(request, "An error has occurred during registration.")

    context = { 'page':  page, 'form': form }
    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "Logout successfully.")
    return redirect('login')
