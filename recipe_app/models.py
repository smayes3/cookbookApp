from django.db import models
from django.urls import reverse

# Create your models here.

#create recipe model
class Recipe(models.Model):
    title = models.CharField(max_length=200, blank=False)
    ingredients = models.TextField(blank=False)
    directions = models.TextField(blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])
    




