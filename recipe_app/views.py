from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *
from django.views import generic
from django.contrib import messages
#from recipe_app.forms import *

# Create your views here.

def index(request):
#render html template index.html with data in context var
    return render(request, 'recipe_app/index.html')


#create generic recipe list and detail views
class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe

