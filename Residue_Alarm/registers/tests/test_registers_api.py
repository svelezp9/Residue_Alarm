from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from core.models import Residue
from registers.serializers import ResidueSerializers

RESIDUE_URL = reverse('registers:residue-list')

class PublicResidueApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
    
    def test_login_required(self):
        res = self.client.get(RESIDUE_URL)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)
    
class PrivateResidueApiTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@mail.com',
            'pass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_residue(self):
        '''Obtener residue'''
        Residue.objects.create(
            img_src = 'r1.jpg',
            user = self.user,
            priority = 1,
            status = 'pending',
            lon = '455.4',
            lat = '66',
        )
        Residue.objects.create(
            img_src = 'r2.jpg',
            user = self.user,
            priority = 2,
            status = 'pending',
            lon = '45.4',
            lat = '656',
        )
        res = self.client.get(RESIDUE_URL)
        residues = Residue.objects.all().order_by('priority')
        serializer = ResidueSerializers(residues,many=True)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data,serializer.data)

    def test_tags_limited_to_user(self):
        '''Probar que si son del usuario esos registros'''
        user2 = get_user_model().objects.create_user(
            'test1@mail.com',
            'pass123'
        )
        Residue.objects.create(
            img_src = 'r2.jpg',
            user = user2,
            priority = 2,
            status = 'pending',
            lon = '45.4',
            lat = '656',
        )
        residue = Residue.objects.create(
            img_src = 'r1.jpg',
            user = self.user,
            priority = 1,
            status = 'pending',
            lon = '454.4',
            lat = '65',
        )
        res = self.client.get(RESIDUE_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(len(res.data),1)
        self.assertEqual(res.data[0]['img_src'],residue.img_src)