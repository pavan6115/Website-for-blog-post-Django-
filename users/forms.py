# this page is created for the additional field that we want to display in the user registeration form
# after the UserRegistration form we created a model form which will work with the database and update it
# class Meta tells us about with which model are we working with and with which all parameters

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# this form will be used for the user's username and email updation
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']

# this form will allow us to update the user's image 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']