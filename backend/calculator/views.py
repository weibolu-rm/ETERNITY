from django.shortcuts import render
from django.http import HttpResponse
import simpleeval as se
import re

#------------------------------------------------------------------------------------------------

# Using Nvidia's fast approximation
# Absolute error <= 6.7e-5
# reference https://developer.download.nvidia.com/cg/acos.html
def arccos(x):
    if x < 0:
        negate = 1
        # get abs val
        x = -x
    else:
        negate = 0

    ret = -0.0187293
    ret = ret * x
    ret = ret + 0.0742610
    ret = ret * x
    ret = ret - 0.2121144
    ret = ret * x
    ret = ret + 1.5707288
    # ret = sqrt(1.0-x)
    if (myPower((1.0-x), 0.5)  != None):
        ret = ret * myPower((1.0-x), 0.5)
        ret = ret - 2 * negate * ret
        return HttpResponse(negate * 3.14159265358979 + ret)
    print("error in arccos")

#------------------------------------------------------------------------------------------------
def abPower(a,b,x):
    result = a * (myPower(b,x))
    return HttpResponse(result)

#------------------------------------------------------------------------------------------------
def log(x,base=10):
    return HttpResponse(ln(x)/ln(base))
def logb(x,base=10):
    return ln(x)/ln(base) 
def ln(x):
    if x<=0 :
        return None

    e = 2.71828182845905
    precision=0.000001
    P=x
    result = 0.0

    while(P >= e):
        P /= e
        result+=1

    result += (P / e)
    P = x

    A = result
    L = (P / (e**(result - 1.0)))
    R = ((result - 1.0) * e)
    result = ((L + R) / e)

    while abs(result-A)>precision:
        A = result
        L = (P / (e**(result - 1.0)))
        R = ((result - 1.0) * e)
        result = ((L + R) / e)

    
    return result
#------------------------------------------------------------------------------------------------
from functools import reduce

# Calculates the mean of the input list and returns it.
def find_mean(input_list):
	return reduce((lambda x, y: x + y), input_list) / len(input_list)

# Find the absolute value of the input.
def absolute(n):
	return n if n >= 0 else -n

# Finds the mean absolute deviation.
def mean_absolute_deviation(input_list):
	mean = find_mean(input_list)
	absolute_difference = 0
	for input in input_list:
		absolute_difference += absolute(input - mean)
	return absolute_difference/len(input_list)

def MAD(x):
    return HttpResponse(mean_absolute_deviation(x))

#------------------------------------------------------------------------------------------------
def standard_deviation(data):
    data = data.split(',')
    N = len(data)
    total = 0
    total_squared = 0
    # Step 1, 2
    for i in data:
        i = int(i)
        total += i  # sum of dataset
        total_squared += i * i  # sum of the square of the dataset
    # Step 3, 4
    sumOfDistances = (total * total) / N
    # Step 5, 6
    variance = (total_squared - sumOfDistances) / N
    # Step 7
    ans = variance ** 0.5
    return HttpResponse(ans)
#------------------------------------------------------------------------------------------------

def sinh(x):
    # Euler's Constant
    e = 2.71828
    # Calculate the result using the previously defined
    # myPow function
    result = (myPower(e,x) - myPower(e,-x))/2
    return HttpResponse(result)

#------------------------------------------------------------------------------------------------
def myPower(x, y):
    
    # Check if the passed in values are integers or decimals
    # Both integers and decimals have different algorithms to calculate their exponentiation
    
    if x % 1 == 0 and y % 1 == 0:
        
        # If y is 0, we can return 0 since 0^x = 0
        
        if x == 0:
  	        return 0
  	        
  	    # If y is 0, we can return 1 since x^0 = 1
  	        
        if y == 0:
  	        return 1
  	        
  	    # Recursively call myPow until y = 0, which by then we will have our integer power.
  	    
        return myPower(x,y-1) * x
        
    # Condition where x or y mod 1 != 0, which means we have a decimal in either x or y    
    
    else:

    # Credit to https://blog.prepscholar.com/natural-log-rules
    # and https://wou.edu/mathcenter/files/2015/09/Exponents-and-Logarithms.pdf for natural log identities used to solve this
    # problem
    
        e = 2.7182818284
        if(ln(x) != None):
            return e ** (y*logb(e,x)) # where e is the base (natural log)

def xPower(x,y):
    return HttpResponse(myPower(x,y))

#------------------------------------------------------------------------------------------------
my_functions = se.DEFAULT_FUNCTIONS.copy()
my_functions.update({"pow":xPower,
                     "sinh":sinh,
                     "MAD":MAD,
                     "log":log,
                     "sd":standard_deviation,
                     "arccos":arccos,
                     "abPow":abPower
                     })

def evaluate(request, expression):
    # replace divide with /
    expression = re.sub(r'divide', '/', expression)
    ans = se.simple_eval(expression,functions = my_functions)
    return HttpResponse(ans)

