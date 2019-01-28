from django.db import models


class Currency(models.Model):
    short_name = models.CharField(max_length=3, unique=True)
    full_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.short_name

    def save(self, *args, **kwargs):
        new = False
        if not self.pk:
            new = True

        super(Currency, self).save(*args, **kwargs)

        if new:
            Rate.objects.create_currency_rates(self)


class RateManager(models.Manager):
    def create_currency_rates(self, new_currency):
        new_rates = list()
        new_rates.append(self.model(master_currency=new_currency, slave_currency=new_currency, rate=1))

        for currency in Currency.objects.all():
            if currency != new_currency:
                new_rates.append(self.model(master_currency=new_currency, slave_currency=currency, rate=0))
                new_rates.append(self.model(master_currency=currency, slave_currency=new_currency, rate=0))

        self.model.objects.bulk_create(new_rates)


class Rate(models.Model):
    master_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rates')
    slave_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rates_as_slave')
    rate = models.FloatField()
    modified_at = models.DateTimeField(auto_now=True)

    objects = RateManager()

    def __str__(self):
        return "Rate {} to {} is {}".format(self.master_currency, 
            self.slave_currency, self.rate)

    def calculate_amount(self, amount):
        return self.rate * amount
