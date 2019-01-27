# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.test')
app = Celery('greenway', broker='amqp://admin:qwerty123@rabbit:5672', backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()    
app.conf.broker_heartbeat = 0
