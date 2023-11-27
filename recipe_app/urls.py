from django.urls import path
from . import views


urlpatterns = [
    #path function: defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.

    path('', views.index, name='index'),

    #add view paths
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/create_recipe/', views.createRecipe, name='create_recipe'),
    path('recipes/delete_recipe/<int:pk>', views.deleteRecipe, name='delete_recipe'),
    path('recipes/update_recipe/<int:pk>', views.updateRecipe, name='update_recipe'),

    #add registration/login/logout pages
    path('accounts/register/', views.registerPage, name='register_page'),
    path('accounts/login/', views.loginPage, name='login'),
    path('accounts/logout/', views.logoutUser, name='logout'),
    
]
