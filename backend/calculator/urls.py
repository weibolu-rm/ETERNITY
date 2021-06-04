from django.urls import path
from .views import function

urlpatterns = [
    path('function/', function)
]
