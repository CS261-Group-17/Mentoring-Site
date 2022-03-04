from django.test import TestCase
from app.models import User

class UserTestCase(TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        self.assertEqual(True, True)
