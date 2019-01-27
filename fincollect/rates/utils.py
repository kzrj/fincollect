import requests
import json

APP_ID = "0b2d9eabbb804384a9b0f32ec024ec7b"

def get_rate(data, master_currency, slave_currency):
    data = json.loads(data)
    return round(data['rates'][master_currency] / data['rates'][slave_currency], 5)
