from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email"]        
class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields= ["profile_pic"]        