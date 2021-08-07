from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from calculator.models import *
import simpleeval as se
import re


def exponential_http(x,y):
    return HttpResponse(exponential(x,y))


def log_http(x,base=10):
    if x<=0:
            return HttpResponseNotAllowed("invalid input for log")

    return HttpResponse(log(x))


def arccos_http(x):
    return HttpResponse(arccos(x))


def a_b_exponential_http(a,b,x):
    result = a * (exponential(b,x))
    return HttpResponse(result)


def mean_absolute_deviation_http(*args):
    return HttpResponse(mean_absolute_deviation(args))


def standard_deviation_http(*args):
    return HttpResponse(standard_deviation(*args))


def sinh_http(x):
    return HttpResponse(sinh(x))

#------------------------------------------------------------------------------------------------
#   SIMPLEEVAL FUNCTION LIBRARY & EVALUTATION FUNCTION
#------------------------------------------------------------------------------------------------

my_functions = se.DEFAULT_FUNCTIONS.copy()
my_functions.update({"pow":exponential_http,
                     "sinh":sinh_http,
                     "MAD":mean_absolute_deviation_http,
                     "log":log_http,
                     "sd":standard_deviation_http,
                     "arccos":arccos_http,
                     "abPow":a_b_exponential_http
                     })

def evaluate(request, expression):
    # replace divide with /
    expression = re.sub(r'divide', '/', expression)
    ans = se.simple_eval(expression,functions = my_functions)
    return HttpResponse(ans)

