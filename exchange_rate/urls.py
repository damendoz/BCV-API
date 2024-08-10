from django.urls import path
from .views import ExchangeRateView

urlpatterns = [
    path('exchange-rate/', ExchangeRateView.as_view(), name='exchange-rate'),
]
