from urllib import request
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    '''Test api público'''

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        payload = {
            'email': 'test@mail.com',
            'password': 'testpass123',
            'name': 'Test name'
        }

        re = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(re.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**re.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',re.data)

    def test_user_exist(self):
        '''Probar crear un usuario que ya existe'''
        payload = {
            'email': 'test@mail.com',
            'password': 'testpass123',
        }
        create_user(**payload)
        re = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(re.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short(self):
        payload = {
            'email': 'test@mail.com',
            'password': 'tes',
            'name': 'test'
        }
        re = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(re.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)


    def test_create_token_for_user(self):
        '''Token si se cree para el usuario'''
        payload = {
            'email': 'test@mail.com',
            'password': 'testepass123',
            'name': 'test'
        }
        create_user(**payload)
        re = self.client.post(TOKEN_URL,payload)
        self.assertIn('token',re.data)
        self.assertEqual(re.status_code, status.HTTP_200_OK)


    def test_create_token_invalid_credentials(self):
        '''Credenciales invalidas'''
        create_user(email='test@mail.com', password='testpass123')
        payload = {
            'email' : 'test@mail',
            'password': 'pass12'
        }
        re = self.client.post(TOKEN_URL,payload)
        self.assertNotIn('token',re.data)
        self.assertEqual(re.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_token_no_user(self):
        '''Prueba que no se crae un token si no existe el user'''
        payload = {
            'email': 'test@mail.com',
            'password': 'testepass123',
            'name': 'test'
        }
        re = self.client.post(TOKEN_URL,payload)
        self.assertNotIn('token',re.data)
        self.assertEqual(re.status_code, status.HTTP_400_BAD_REQUEST)
    

    def test_create_token_missing_field(self):
        '''Probar que el email y password sean requeridos'''
        payload = {
            'email': 'test',
            'password': '',
        }
        re = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token',re.data)
        self.assertEqual(re.status_code, status.HTTP_400_BAD_REQUEST)
    