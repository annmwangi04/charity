from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="users-register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"),  # Django's built-in login
    path("logout/", views.logout_user, name="users-logout"),
    path("profile/", views.user_profile, name="users-profile"),
]
