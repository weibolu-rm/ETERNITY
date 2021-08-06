from django.shortcuts import render
from django.http import HttpResponse
import simpleeval as se
import re


euler = 2.718281828459045235360
pi    = 3.141592653589793

#------------------------------------------------------------------------------------------------
#    HELPER FUNCTIONS: ceil & floor
#------------------------------------------------------------------------------------------------

def ceil(n):
    return int(-1 * n // 1 * -1)

def floor(n):
    return int(n // 1)

def absolute(n):
	return n if n >= 0 else -n

#------------------------------------------------------------------------------------------------
#    EXPONENTIAL FUNCTION: X^Y
#------------------------------------------------------------------------------------------------

def exponential(x, y):
    
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
  	    
        return exponential(x,y-1) * x
        
    # Condition where x or y mod 1 != 0, which means we have a decimal in either x or y    
    
    else:

    # Credit to https://blog.prepscholar.com/natural-log-rules
    # and https://wou.edu/mathcenter/files/2015/09/Exponents-and-Logarithms.pdf for natural log identities used to solve this
    # problem
    
        if(ln(x) != None):
            return exponential(euler,(y*log(euler,x))) # where e is the base (natural log)

def taylor_exp(x):    
     
      if x == 0:
          return 1
      
      x0 = absolute(x)
     
      Tn = 1
      
      n = ceil(x0 * euler) * 12
      for k in range(n, 0, -1):
          Tn = Tn * (x0 / k) + 1
     
      if x < 0:
          Tn = 1 / Tn
      return Tn

# def exponential(a,x):
#     if x==0:
#         return 1
#     if a==0:
#         return 0

#     if a<0:
#         x_floor= floor(x)
        
#         if x_floor%2 == 0:
#             sign=1
#         else:
#             sign=-1
        
#         if x != x_floor:
#             ## The case where a is negative and x has a fraction is not covered, since the answer might be an imaginary number.
#             print("Error out of range")
#             return
#         temp=ln(-a)*x

#         return sign*taylor_exp(temp)
#     else:   
#         temp=ln(a)*x
#         return taylor_exp(temp)

def exponential_http(x,y):
    return HttpResponse(exponential(x,y))

#------------------------------------------------------------------------------------------------\
#   INVERSE COSINE FUNCTION: ARCCOS(X)
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
    # THIS CONDITIONAL STATEMENT IS BEING USED TO HANDLE INVALID INPUT
    if (exponential((1.0-x), 0.5)  != None):
        ret = ret * exponential((1.0-x), 0.5)
        ret = ret - 2 * negate * ret
        return HttpResponse(negate * 3.14159265358979 + ret)
    print("error in arccos")

#------------------------------------------------------------------------------------------------
# SPECIAL EXPONENTIAL FUNCTION: AB^X
#------------------------------------------------------------------------------------------------

def a_b_exponential(a,b,x):
    result = a * (exponential(b,x))
    return HttpResponse(result)

def euler_exponential(exponent):
    a = 1
    b = euler
    return a * exponential(b, exponent)


def ten_exponential(exponent):
    a = 1
    b = 10
    return a * exponential(b, exponent)


def pi_exponential(exponent):
    a = 1
    b = pi
    return a * exponential(b, exponent)

#------------------------------------------------------------------------------------------------
#   LOGARITHMIC FUNCTIONS: LN(X) and LOG(X)
#------------------------------------------------------------------------------------------------

def log_http(x,base=10):
    return HttpResponse(ln(x)/ln(base))

def log(x,base=10):
    return ln(x)/ln(base) 

def ln(x):
    if x<=0 :
        return None

    precision=0.000001
    P=x
    result = 0.0

    while(P >= euler):
        P /= euler
        result+=1

    result += (P / euler)
    P = x

    A = result
    L = (P / exponential(euler,(result - 1.0)))
    R = ((result - 1.0) * euler)
    result = ((L + R) / euler)

    while abs(result-A)>precision:
        A = result
        L = (P / exponential(euler,(result - 1.0)))
        R = ((result - 1.0) * euler)
        result = ((L + R) / euler)
    return result

#------------------------------------------------------------------------------------------------
#    MEAN ABSOLUTE DEVIATION FUNCTION: MAD(x)
#------------------------------------------------------------------------------------------------

from functools import reduce

# Calculates the mean of the input list and returns it.
def find_mean(input_list):
	return reduce((lambda x, y: x + y), input_list) / len(input_list)


# Finds the mean absolute deviation.
def mean_absolute_deviation(input_list):
	mean = find_mean(input_list)
	absolute_difference = 0
	for input in input_list:
		absolute_difference += absolute(input - mean)
	return absolute_difference/len(input_list)

def mean_absolute_deviation_http(x):
    return HttpResponse(mean_absolute_deviation(x))

#------------------------------------------------------------------------------------------------
# STANDARRD DEVIATION FUNCTION: σ(x)
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
    return ans

def standard_deviation_http(data):
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
#   HYPERBOLIC SINE FUNCTION: sinh(x)
#------------------------------------------------------------------------------------------------

def sinh(x):
    # Calculate the result using the previously defined
    # myPow function
    result = (exponential(euler,x) - exponential(euler,-x))/2
    return HttpResponse(result)

#------------------------------------------------------------------------------------------------
#   SIMPLEEVAL FUNCTION LIBRARY & EVALUTATION FUNCTION
#------------------------------------------------------------------------------------------------

my_functions = se.DEFAULT_FUNCTIONS.copy()
my_functions.update({"pow":exponential_http,
                     "sinh":sinh,
                     "MAD":mean_absolute_deviation_http,
                     "log":log_http,
                     "sd":standard_deviation,
                     "arccos":arccos,
                     "abPow":a_b_exponential
                     })

def evaluate(request, expression):
    # replace divide with /
    expression = re.sub(r'divide', '/', expression)
    ans = se.simple_eval(expression,functions = my_functions)
    return HttpResponse(ans)

