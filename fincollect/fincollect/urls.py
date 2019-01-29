from django.contrib import admin
from django.urls import path

from rates.views import CurrencyList, RateRetrieve, update_rates_now

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/currencies/', CurrencyList.as_view()),
    path('api/rate/', RateRetrieve.as_view()),
    path('api/update_rates_now/', update_rates_now),
]
