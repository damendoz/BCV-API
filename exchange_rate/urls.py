from django.urls import path
from .views import ExchangeRateView

urlpatterns = [
    path('', ExchangeRateView.as_view(), name='exchange-rate'),
]
