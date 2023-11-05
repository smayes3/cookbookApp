from django.forms import ModelForm
from .models import *

#create class for the recipe form
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'directions')