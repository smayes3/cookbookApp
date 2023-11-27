from django.test import TestCase
from recipe_app.forms import CreateUserForm


#create tests for user registration form
class CreateUserFormTest(TestCase):
    def test_create_user_form_password1_field(self):
        form = CreateUserForm()
        self.assertTrue(form.fields['password1'].label is None or form.fields['password1'].label == 'Password')
