from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


class SnacksTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="snack eater", email="", password="snacks")
        self.snack = Snack.objects.create(
            name='Corn Bread', description="Bread made from corn meal", purchaser=self.user)

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'Corn Bread')

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'Bread made from corn meal')

    def test_string_representation(self):
        self.assertEqual(f'{str(self.snack)}', 'Corn Bread')