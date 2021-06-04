from django.shortcuts import render
from django.http import HttpResponse
import simpleeval as se
import re


def arccos(x):
    return HttpResponse(x)


def abPower(x):
    return HttpResponse(x)


def log(b, x):
    return HttpResponse(b)


def MAD(x):
    return HttpResponse(x)


def standardDeviation(x):
    return HttpResponse(x)


def sinh(x):
    return HttpResponse(x)


def xPower(request, x, y):
    x ** y
    return HttpResponse(x)


def evaluate(request, expression):
    # replace divide with /
    expression = re.sub(r'divide', '/', expression)
    ans = se.simple_eval(expression)
    return HttpResponse(ans)
