from django.test import TestCase
from ..models import Menu


# Create your tests here.
class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=9, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 9")
