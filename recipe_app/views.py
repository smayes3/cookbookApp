from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *
from django.views import generic
from django.contrib import messages
from recipe_app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
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


#create view for creating a user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid:
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        

        context = {'form':form}
        return render(request, 'registration/register.html', context)


#create view for login
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username OR password is incorrect!")

        context = {}
        return render(request, 'registration/login.html', context)


#create view for logout
def logoutUser(request):
    logout(request)
    return redirect('login')