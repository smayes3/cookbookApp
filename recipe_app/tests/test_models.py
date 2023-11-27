from django.test import TestCase

#import models
from recipe_app.models import Recipe


#test the recipe model
class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #set up non-modded objs used by all test methods
        Recipe.objects.create(title="TestRecipe")
    
    def test_title_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_ingredients_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name
        self.assertEqual(field_label, 'ingredients')

    def test_directions_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('directions').verbose_name
        self.assertEqual(field_label, 'directions')

    def test_get_abs_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/recipe/1')



