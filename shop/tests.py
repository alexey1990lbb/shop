from django.test import TestCase

class SimpleTest(TestCase):
    def test_math(self):
        self.assertEqual(2 + 2, 4)

    def test_homepage(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 404])