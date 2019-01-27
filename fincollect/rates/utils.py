import requests
import json

APP_ID = "0b2d9eabbb804384a9b0f32ec024ec7b"


def get_latest(APP_ID):
    response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % APP_ID)
    if response.ok:
        return True, json.loads(response.text)
    else:
        return False, response.text

def get_rate(data, master_currency, slave_currency):
    return data['rates'][slave_currency] / data['rates'][master_currency]


class RawRates():
    def __init__(self, app_id):
        self.app_id = app_id
        self.data = {}
        self.errors = {}

    def check_response(self, response):
        if response.ok:
            self.data = json.loads(response.text)
            return True
        else:
            self.errors = {'status_code': response.status_code, 'text': response.text}
            return False

    def get_latest(self):
        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s' % self.app_id)
        # return self.check_response(response)
        if response.ok:
            self.data = json.loads(response.text)
            return True
        else:
            self.errors = {'status_code': response.status_code, 'text': response.text}
            return False

    def get_rate(self, slave_currency, master_currency):
        return self.data['rates'][slave_currency] / self.data['rates'][master_currency]
