# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery import shared_task

from django.apps import apps

from django_bulk_update.helper import bulk_update

from .models import Currency, Rate
from .utils import APP_ID, get_rate


@shared_task
def get_latest_rates():
    response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % APP_ID)
    if response.ok:
        rates = Rate.objects.select_related('master_currency').select_related('slave_currency').all()
        for rate in rates:
            rate.rate = get_rate(response.text, rate.master_currency.short_name, rate.slave_currency.short_name)

        bulk_update(rates, update_fields=['rate'])

    else:
        pass
        # retry and log
