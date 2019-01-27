from django.contrib import admin
from django.urls import path

from rates.views import CurrencyList, RateRetrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/currencies/', CurrencyList.as_view()),
    path('api/rate/', RateRetrieve.as_view()),
]
