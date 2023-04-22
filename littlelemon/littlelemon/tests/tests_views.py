from django.test import TestCase
import tests_models

class MenuViewTest(TestCase):
    def setUp(self) -> tests_models:
        return super().setUp(item = "Icecream")