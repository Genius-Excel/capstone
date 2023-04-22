from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def get_get(self):
        item = Menu.objects.create(title = "Icecream", price = 80 , invenetory = 100)
        self.assertEqual(item, "Icecream : 80")