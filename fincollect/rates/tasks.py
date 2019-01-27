# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery import shared_task

from django.apps import apps

from django_bulk_update.helper import bulk_update

from .models import Currency, Rates
from .utils import RawRates, APP_ID, get_latest, get_rate


@shared_task
def get_latest_rates():
    raw_rates = RawRates(APP_ID)
    if raw_rates.get_latest():
        rates = Rates.objects.select_related('master_currency').select_related('slave_currency').all()
        for rate in rates:
            rate.rate = raw_rates.get_rate(rate.slave_currency, rate.master_currency)

        bulk_update(rates, update_fields=['rate'])

    else:
        pass
        # retry and log
