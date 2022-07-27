from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User


class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','password1', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

