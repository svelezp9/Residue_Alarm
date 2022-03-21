from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@mail.com',
            password = 'Testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@mail.com',
            password = 'Testpass123',
            name = 'Test1'
        )
    def test_users_listed(self):
        '''Test que los usuraios están enlistados en la página usuarios de admin'''

        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response,self.user.name)
        self.assertContains(response,self.user.email)
    def test_user_change_page(self):
        '''Test que la página editada por el user funciona'''
        url = reverse('admin:core_user_change',args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    def test_create_user_page(self):
        '''Test que la página de crear usuario funciona'''
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)