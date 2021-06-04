from django.shortcuts import render
from django.http import HttpResponse


def function(request):
    msg = """{
            "value": "Hello World from Django!"
        }"""
    return HttpResponse(msg)
