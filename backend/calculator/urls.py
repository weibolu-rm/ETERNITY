from django.urls import path
from .views import arccos, a_b_exponential, log_http, mean_absolute_deviation_http, standard_deviation_http, sinh, exponential_http, evaluate

urlpatterns = [
    path('arccos/', arccos),
    path('abPowerx/', a_b_exponential),
    path('log/', log_http),
    path('MAD/', mean_absolute_deviation_http),
    path('standard_deviation/', standard_deviation_http),
    path('sinh/', sinh),
    path('<int:x>power<int:y>/', exponential_http),
    path('<str:expression>/', evaluate)
]
