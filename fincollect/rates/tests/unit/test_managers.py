from django.test import TestCase

from rates.models import Rate, Currency


class ManagersTest(TestCase):
    fixtures = ['currencies', 'rates']

    def test_rateManager_create_currency_rates(self):

        # The model’s save() method will not be called
        Currency.objects.bulk_create([Currency(short_name="RUB", full_name="Russian Ruble")])

        new_currency = Currency.objects.get(short_name="RUB", full_name="Russian Ruble")

        Rate.objects.create_currency_rates(new_currency)

        new_rates_master_count = Rate.objects.filter(master_currency=new_currency).count()
        # rates for each of init 4 currencies + 1 self/self rate
        self.assertEqual(new_rates_master_count, 5)

        new_rates_slave_count = Rate.objects.filter(slave_currency=new_currency).count()
        self.assertEqual(new_rates_slave_count, 5)
