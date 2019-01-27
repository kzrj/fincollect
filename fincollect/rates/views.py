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
    	print(request.GET)
    	serializer = RateSerializer(data=request.GET)
    	if serializer.is_valid():
    		print('Valid')
    	else:
    		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    	
    	return Response(request.GET)