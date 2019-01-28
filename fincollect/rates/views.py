from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency, Rate
from .serializers import CurrencySerializer, RateSerializer


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class RateRetrieve(APIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def get(self, request, format=None):
        serializer = RateSerializer(data=request.GET)
        if serializer.is_valid():
            rate = Rate.objects.filter(master_currency=serializer.validated_data['master_currency'],
                slave_currency=serializer.validated_data['slave_currency']).first()
            amount = rate.calculate_amount(serializer.validated_data['amount'])

            return Response({
                'id': rate.pk,
                'master_currency': rate.master_currency.short_name,
                'slave_currency': rate.slave_currency.short_name,
                'rate': rate.rate,
                'total_amount': amount
            })

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
