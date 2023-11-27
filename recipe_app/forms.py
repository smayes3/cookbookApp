from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.models import User


#create class for the recipe form
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'directions']


#create class for the user registration form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


