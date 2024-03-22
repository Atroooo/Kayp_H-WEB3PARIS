from django.test import TestCase
from django.contrib.auth.models import User
from authentication.forms import CustomUserCreationForm
import os
class CustomUserCreationFormTest(TestCase):
    def setUp(self):
        # Create a user for duplicate checks
        self.existing_user = User.objects.create_user(username='existinguser', email='existing@example.com', password='existingpassword')


    def test_valid_form(self):
        # Test with valid data
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@example.com')

    def test_required_fields(self):
        # Test if form data missing required fields is invalid
        form_data = {}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    def test_password_match(self):
        # Test if passwords match
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'DifferentPassword123!',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_email_format(self):
        # Test if the form requires a valid email format
        invalid_email_data = {
            'username': 'newuser',
            'email': 'invalidemail',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }

        form = CustomUserCreationForm(data=invalid_email_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_username_uniqueness(self):
        # Test if the form enforces unique usernames
        duplicate_username_data = {
            'username': 'existinguser',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }

        form = CustomUserCreationForm(data=duplicate_username_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_save_method(self):
        # Test if the form's save method works
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }

        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@example.com')
