from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *
from django.views import generic
from django.contrib import messages
from recipe_app.forms import *

# Create your views here.

def index(request):
#render html template index.html with data in context var
    return render(request, 'recipe_app/index.html')


#create generic recipe list and detail views
class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe

#create view for new recipe using forms
def createRecipe(request):
    #create a new recipe form
    form = RecipeForm()

    #form handling
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        #check if the form is valid
        if form.is_valid():
            #Save the recipe to db
            form.save()
            #redirect back to recipe list view page
            return redirect(reverse('recipes'))
            #return redirect(reverse('recipes'))
        
    #update dictionary
    context = {'form': form}
    
    #render the form
    return render(request, 'recipe_app/recipe_form.html', context)


#create view to delete recipe
def deleteRecipe(request, pk):
    #get recipe to delte
    recipe = get_object_or_404(Recipe, pk=pk)

    #set dictionary vals
    context = {'title': recipe.title}

    #handle deleting 
    if request.method == "POST":
        
        recipe.delete()

        #redirect to recipe list
        return redirect(reverse('recipes'))
    
    #display delete confirmation
    return render(request, 'recipe_app/recipe_delete.html', context)


#create view to update recipe
def updateRecipe(request, pk):
    #init dictionary
    context = {}

    #get recipe to update
    recipe = get_object_or_404(Recipe, pk=pk)

    #pass recipe as form instance
    form = RecipeForm(request.POST or None, instance=recipe)

    #save form data and redirect
    if form.is_valid():
        form.save()
        return redirect(reverse('recipes'))
    
    #add form to dictionary and render
    context["form"] = form
    return render(request, 'recipe_app/recipe_update.html', context)

