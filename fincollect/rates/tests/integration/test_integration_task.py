import requests

from django.test import TestCase

from rates.tasks import get_latest_rates
from rates.models import Rate
from rates.utils import APP_ID, get_latest, get_rate


class TasksTest(TestCase):
    fixtures = ['currencies', 'rates']

    def test_get_latest_rates(self):
        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % APP_ID)
        external_api_rate = get_rate(data=response.text, slave_currency='EUR', master_currency='USD')
        
        get_latest_rates()
        db_rate = Rate.objects.get(master_currency__short_name='USD', slave_currency__short_name='EUR')
        self.assertEqual(round(external_api_rate, 5), db_rate.rate)
