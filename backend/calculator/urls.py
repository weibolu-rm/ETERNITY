from django.urls import path
from .views import *

urlpatterns = [
    path('arccos/', arccos_http),
    path('abPowerx/', a_b_exponential_http),
    path('log/', log_http),
    path('MAD/', mean_absolute_deviation_http),
    path('standard_deviation/', standard_deviation_http),
    path('sinh/', sinh_http),
    path('<int:x>power<int:y>/', exponential_http),
    path('<str:expression>/', evaluate)
]
