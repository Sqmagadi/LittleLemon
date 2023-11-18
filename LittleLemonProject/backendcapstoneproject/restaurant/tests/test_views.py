from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Menu
from ..serializers import MenuSerializer


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/restaurant/')
        self.assertEqual(response.status_code, 200)


class MenuViewTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        Menu.objects.create(title='Menu Z', price=30, inventory=10)
        Menu.objects.create(title='Menu Y', price=10, inventory=100)
        Menu.objects.create(title='Menu X', price=20, inventory=1000)
        Menu.objects.create(title='Menu W', price=5, inventory=5)

    # def tearDown(self):
    #     # Clean up run after every test method.
    #     pass

    def test_get_all(self):
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        self.assertEqual(response.data, expected_data)
