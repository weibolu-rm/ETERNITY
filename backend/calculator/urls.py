from django.urls import path
from .views import arccos, abPower, log, MAD, standard_deviation, sinh, xPower, evaluate

urlpatterns = [
    path('arccos/', arccos),
    path('abPowerx/', abPower),
    path('log/', log),
    path('MAD/', MAD),
    path('standard_deviation/', standard_deviation),
    path('sinh/', sinh),
    path('<int:x>power<int:y>/', xPower),
    path('<str:expression>/', evaluate)
]
