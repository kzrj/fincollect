from rest_framework import serializers

from .models import Currency, Rate


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['master_currency', 'slave_currency']
