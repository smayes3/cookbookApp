from django.forms import ModelForm, modelformset_factory
from .models import *
from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.models import User


#create class for the recipe form
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'createdBy', 'ingredients', 'directions']
        labels = {'createdBy': "Created by"}


#create class for the user registration form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


