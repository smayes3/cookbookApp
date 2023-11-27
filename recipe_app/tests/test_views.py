from django.test import TestCase
from django.contrib.auth import get_user_model
from recipe_app.models import Recipe
from django.urls import reverse

#create test for restricted recipe creation view
User = get_user_model()

class CreateRecipeViewTest(TestCase):
    #create a test user
    def setUp(self):
        user1 = User.objects.create(
            username="testUser1", 
            email="user1@test.com", 
            password="testPW123", 
            #password2="testPW123"
            )
        user2 = User.objects.create(
            username="testUser2", 
            email="user2@test.com", 
            password="testPW123", 
            #password2="testPW123"
            )

        user1.save()
        user2.save()

        #create a recipe
        recipe = Recipe.objects.create(
            title="testRecipe",
            ingredients="ingr1, ingr2",
            directions="step1, step2"
        )

        recipe.save()

    def test_redirect_if_not_login(self):
        response = self.client.get(reverse('create_recipe'))
        self.assertRedirects(response, '/accounts/login/?next=/recipes/create_recipe/')

    # def test_logged_uses_correct_template(self):
    #     login = self.client.login(username='user1', password='testPW123')
    #     response = self.client.get(reverse('create_recipe'))

    #     #check if user logged in
    #     self.assertEqual(response.context['username'], 'user1')

    #     #check if respinse is success
    #     self.assertEqual(response.status_code, 200)

    #     #check correct template used
    #     self.assertTemplateUsed(response, 'recipe_app/recipe_form.html')