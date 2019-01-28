from rest_framework import serializers

from .models import Currency, Rate


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(min_value=0)

    class Meta:
        model = Rate
        fields = ['master_currency', 'slave_currency', 'amount']