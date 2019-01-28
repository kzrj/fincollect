import requests

from django.test import TestCase

from rates.utils import get_rate, APP_ID


class UtilsIntegrationTest(TestCase):
    def test_get_rate(self):
        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % APP_ID)

        rate = get_rate(response.text, 'USD', 'USD')
        self.assertEqual(rate, 1)
        self.assertIsInstance(rate, float)
