import logging

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

logger = logging.getLogger(__name__)


class RatesViewTests(APITestCase):
    fixtures = ['currencies', 'rates']

    def setUp(self):
        self.client = APIClient()

    def test_currencies_list(self):
        response = self.client.get('/api/currencies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 4)

    def test_rate_retrieve(self):
        response = self.client.get('/api/rate/', data={'master_currency': 1,
        	'slave_currency': 1, 'amount': 1})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['total_amount'], 1)
        self.assertEqual(response.data['rate'], 1)
        self.assertEqual(response.data['master_currency'], 'USD')
        self.assertEqual(response.data['slave_currency'], 'USD')
