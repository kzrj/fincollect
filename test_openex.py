import requests
import json

APP_ID = "0b2d9eabbb804384a9b0f32ec024ec7b"

def get_currencies():
    response = requests.get('https://openexchangerates.org/api/currencies.json')

    print(response.text)

# USD, EUR, PLN, CZK

def get_latest(APP_ID):
    response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % APP_ID)
    return json.loads(response.text)


class RawRates():
    def __init__(self, app_id):
        self.app_id = app_id
        self.data = {}
        self.errors = {}

    def check_response(self, response):
        if response.status_code == 200:
            self.data = json.loads(response.text)
            return True
        else:
            self.errors = {'status_code': response.status_code, 'text': response.text}
            return False

    def get_latest(self):
        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % self.app_id)
        return self.check_response(response)

    def get_rate(self, master_currency, slave_currency):
        return self.data['rates'][slave_currency] / self.data['rates'][master_currency]


def get_rate(date, master_currency, slave_currency):
    return data['rates'][slave_currency] / data['rates'][master_currency]

rates = RawRates(APP_ID)

if rates.get_latest():
    print(rates.get_rate('USD', 'PLN'))
else:
    print(rates.errors)