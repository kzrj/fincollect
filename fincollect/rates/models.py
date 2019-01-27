from django.db import models


class Currency(models.Model):
    short_name = models.CharField(max_length=3)
    full_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.short_name


class Rate(models.Model):
    master_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rates')
    slave_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rates_as_slave')
    rate = models.FloatField()
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Rate {} to {} is {}".format(self.master_currency, 
            self.slave_currency, self.rate)
