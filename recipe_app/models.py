from django.db import models
from django.urls import reverse

# Create your models here.

#create recipe model
class Recipe(models.Model):
    title = models.TextField(blank=False, help_text="Enter title of recipe.")
    ingredients = models.TextField(blank=False, help_text="Enter the ingredients.")
    directions = models.TextField(blank=False, help_text="Enter the directions.")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])
    




