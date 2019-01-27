from django.test import TestCase

from rates.utils import get_latest, get_rate, APP_ID


class UtilsIntegrationTest(TestCase):
    def test_get_rate(self):
        success, data = get_latest(APP_ID)
        rate = get_rate(data, 'USD', 'USD')
        self.assertEqual(rate, 1)
        self.assertIsInstance(rate, float)
