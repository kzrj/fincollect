from django.test import TestCase

from unittest.mock import Mock, patch

from rates.utils import get_rate


class UtilsTest(TestCase):
    def test_get_rate(self):
        data = '{"rates": {"USD": 1}}'
        rate = get_rate(data, 'USD', 'USD')
        self.assertEqual(rate, 1)
        self.assertIsInstance(rate, float)
