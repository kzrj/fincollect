from django.test import TestCase

from rates.models import Currency, Rate


class ModelsTest(TestCase):
    fixtures = ['currencies', 'rates']

    def test_rate_calculate_amout(self):
        rate = Rate.objects.all().first()
        total_amount = rate.calculate_amount(5)        

        self.assertEqual(rate.rate, 1)
        self.assertEqual(total_amount, 5)
        self.assertIsInstance(total_amount, float)

    def test_currency_save(self):
        '''
            Should create rates when new currency has created
        '''
        new_currency = Currency.objects.create(short_name="RUB", full_name="Russian Ruble")
        
        new_rates_master_count = Rate.objects.filter(master_currency=new_currency).count()
        # rates for each of init 4 currencies + 1 self/self rate
        self.assertEqual(new_rates_master_count, 5)

        new_rates_slave_count = Rate.objects.filter(slave_currency=new_currency).count()
        self.assertEqual(new_rates_slave_count, 5)
