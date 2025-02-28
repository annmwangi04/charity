from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UpdateUserForm, UpdateUserProfile

# 🚀 Register a New User
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Registration successful for {user.username}. You can now log in.")
            return redirect("users-login")  # Redirect to login page
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {'form': form})

# 🔑 Login User
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("index")  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {'form': form})

# 🚪 Logout User
def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("users-login")  # Redirect to login page after logout

# 👤 User Profile (Update User Info)
@login_required
def user_profile(request):
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateUserProfile(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("users-profile")  # Redirect to profile page
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateUserProfile(instance=request.user.profile)
    
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile.html", context)
