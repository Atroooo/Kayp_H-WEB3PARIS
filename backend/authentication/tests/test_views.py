from django.test import TestCase, Client
from django.urls import reverse
from authentication import tokens
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import json
import os

class testViews(TestCase):
    
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            is_active=True,
        )
        self.userAPI = get_user_model().objects.create_user(
            username='testuserAPI',
            password='',
            is_active=True,
        )
        self.user_not_active = get_user_model().objects.create_user(
            username='testuser_not_active',
            password='testpassword',
            is_active=False,
        )
        self.user_not_unique = get_user_model().objects.create_user(
            username='notunique',
            password='notunique',
            is_active=False,
        )

    # ACTIVATE_ACCOUNT
    def test_activate_account_success(self):
        token = tokens.account_activation_token.make_token(self.user)
        # Create a URL with uidb64 and token
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = f'https://127.0.0.1:8000/authentication/activate_account/{uidb64}/{token}/'

        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.get(pk=self.user.pk).is_active)
        
    def test_activate_account_wrong_token(self):
        token = f"{tokens.account_activation_token.make_token(self.user)}wrong"
        # Create a URL with uidb64 and token
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = f'https://127.0.0.1:8000/authentication/activate_account/{uidb64}/{token}/'

        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_register_token_invalid_method(self):
        client = Client()
        url = reverse('activate_account', args=['uidb64', 'token'])
        response = client.post(url, None, content_type='application/json')
        self.assertEqual(response.status_code, 405)
    
    #REGISTER_USER
    @patch('authentication.tasks.delete_account_if_not_activate.apply_async', side_effect=lambda *args, **kwargs: None)
    def test_register_user_valid_credentials_success(self, mock_delete_account_if_not_activate):
        client = Client()
        url = reverse('register_user')
        data = {'username': 'test@gmail.com', 'password1': 'Testpassword69' ,'password2' : 'Testpassword69' }
        json_data = json.dumps({"userData": data})
        response = client.post(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    @patch('authentication.tasks.delete_account_if_not_activate.apply_async', side_effect=lambda *args, **kwargs: None)
    def test_register_user_wrong_credentials(self, mock_delete_account_if_not_activate):
        client = Client()
        url = reverse('register_user')
        data = {'username': 'test@gmail.com', 'password1': 'Testpassword' ,'password2' : 'Testpassword69'}
        json_data = json.dumps({"userData": data})
        response = client.post(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    @patch('authentication.tasks.delete_account_if_not_activate.apply_async', side_effect=lambda *args, **kwargs: None)
    def test_register_user_already_used_username(self, mock_delete_account_if_not_activate):
        client = Client()
        url = reverse('register_user')
        data = {'username': 'sameUser', 'password1': 'Testpassword69' ,'password2' : 'Testpassword69' ,'email': 'notsameEmail@test.test'}
        json_data = json.dumps({"userData": data})
        response = client.post(url, json_data, content_type='application/json')

        data = {'username': 'sameUser', 'password1': 'Testpassword69' ,'password2' : 'Testpassword69' ,'email': 'sameEmail@test.test'}
        json_data = json.dumps({"userData": data})
        response = client.post(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_register_user_invalid_method(self):
        client = Client()
        response = client.get(reverse('register_user'))
        self.assertEqual(response.status_code, 405)

    def test_register_user_invalid_JSON(self):
        client = Client()
        url = reverse('register_user')
        response = client.post(url, None)
        self.assertEqual(response.status_code, 400)

    def test_register_user_missing_credential(self):
        client = Client()
        url = reverse('register_user')
        data = {'password1': 'Testpassword69' ,'password2' : 'Testpassword69' ,'email': 'notsameEmail@test.test'}
        json_data = json.dumps({"userData": data})
        response = client.post(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    #LOGIN_USER
    def test_login_user_valid_credentials_success(self):
        client = Client()
        url = reverse('login_user')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_user_missing_credentials(self):
        client = Client()
        url = reverse('login_user')
        data = {}
        response = client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_user_invalid_credentials(self):
        client = Client()
        url = reverse('login_user')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_user_invalid_method(self):
        client = Client()
        response = client.get(reverse('login_user'))
        self.assertEqual(response.status_code, 405)
    
    def test_login_user_invalid_json(self):
        client = Client()
        url = reverse('login_user')
        response = client.post(url, None)
        self.assertEqual(response.status_code, 400)
    
    #LOGOUT_USER
    def test_logout_user_success(self):
        client = Client()
        url = reverse('logout_user')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_logout_user_invalid_method(self):
        client = Client()
        response = client.post(reverse('logout_user'))
        self.assertEqual(response.status_code, 405)

    
    # # FORGOT_PASSWORD
    # # @patch('authentication.views.send_forgot_password_email')
    # def test_forgot_password_success(self):
    #     client = Client()
    #     url = reverse('forgot_password')
    #     data = {'username': 'test@test.test'}
    #     response = client.post(url, json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
        
    # def test_forgot_password_invalid_json(self):
    #     client = Client()
    #     url = reverse('forgot_password')
    #     response = client.post(url, None)
    #     self.assertEqual(response.status_code, 400)
    
    # # RESET_PASSWORD
    # def test_reset_password_success(self):
    #     client = Client()
    #     token = tokens.reset_password_token.make_token(self.user)
    #     uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
    #     url = f'https://127.0.0.1:8000/authentication/reset_password/{uidb64}/{token}/'
    #     data = {'password1': 'newpassword', 'password2': 'newpassword'}
    #     response = client.post(url, json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
        
    # def test_reset_password_invalid_token(self):
    #     client = Client()
    #     token = f'{tokens.reset_password_token.make_token(self.user)}wrong'
    #     uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
    #     url = f'https://127.0.0.1:8000/authentication/reset_password/{uidb64}/{token}/'
    #     data = {'password1': 'newpassword', 'password2': 'newpassword'}
    #     response = client.post(url, json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
        
    # def test_reset_password_invalid_method(self):
    #     client = Client()
    #     token = f'{tokens.reset_password_token.make_token(self.user)}wrong'
    #     uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
    #     url = f'https://127.0.0.1:8000/authentication/reset_password/{uidb64}/{token}/'
    #     response = client.get(url)
    #     self.assertEqual(response.status_code, 405)
        
    # def test_reset_password_invalid_json(self):
    #     client = Client()
    #     token = f'{tokens.reset_password_token.make_token(self.user)}'
    #     uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
    #     url = f'https://127.0.0.1:8000/authentication/reset_password/{uidb64}/{token}/'
    #     response = client.post(url, None)
    #     self.assertEqual(response.status_code, 400)


    #CSRF TOKEN
    def test_get_csrf_token_success(self):
        client = Client()
        response = client.get(reverse('get_csrf_token'))
        self.assertEqual(response.status_code, 200)

    def test_get_csrf_token_invalid_method(self):
        client = Client()
        url = reverse('get_csrf_token')
        response = client.post(url, None, content_type='application/json')
        self.assertEqual(response.status_code, 405)


# class ChangePasswordViewTest(TestCase):

#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='test@test.test',
#             password='testpassword',
#             is_active=True,
#         )

#     def test_change_password_success(self):
#         self.client.force_login(self.user)
#         url = reverse('change_password')
#         data = {'old_password': 'testpassword', 'new_password': 'newpassword'}
#         response = self.client.put(url, json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(get_user_model().objects.get(pk=self.user.pk).check_password('newpassword'))

#     def test_change_password_wrong_old_password(self):
#         self.client.force_login(self.user)
#         url = reverse('change_password')
#         data = {'old_password': 'wrongpassword', 'new_password': 'newpassword'}
#         response = self.client.put(url, json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 400)

#     def test_change_password_invalid_json(self):
#         self.client.force_login(self.user)
#         url = reverse('change_password')
#         response = self.client.put(url, None, content_type='application/json')
#         self.assertEqual(response.status_code, 400)

