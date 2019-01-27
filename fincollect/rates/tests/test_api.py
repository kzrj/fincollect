import logging

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

logger = logging.getLogger(__name__)


class RatesViewTests(APITestCase):
    fixtures = ['currencies', 'rates']

    def setUp(self):
        self.client = APIClient()

    def test_currencies(self):
        response = self.client.get('/api/currencies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 4)

    def test_rate(self):
        response = self.client.get('/api/rate/', data={'master_currency': 'USD',
        	'slave_currency': 'USD'})
        
        logger.error("LOG %s" % response.data)
        self.assertEqual(response.status_code, 200)