from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
#render html template index.html with data in context var
    return render(request, 'recipe_app/index.html')
