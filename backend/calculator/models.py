from django.db import models

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

#------------------------------------------------------------------------------------------------
#    EXPONENTIAL FUNCTION: X^Y
#------------------------------------------------------------------------------------------------

def exponential(a,x):

    if x%1 == 0 and a%1 == 0:
        return exponential_int(a,x)
    else:
        if x==0:
            return 1
        if a==0:
            return 0

        if a<0:
            x_floor= floor(x)

            if x_floor%2 == 0:
                sign=1
            else:
                sign=-1

            if x%1 != 0:
                ## The case where a is negative and x has a fraction is not covered, since the answer might be an imaginary number.
                return -1 * exponential(-a,x)
            temp=ln(-a)*x
            return sign*taylor_exp(temp)
        else:
            temp=ln(a)*x
            return taylor_exp(temp)

def exponential_int(x,y):
    z = x

    if y == 0:
        return 1

    for i in range(1,absolute(int(y))):
        print("i : " + str(i))
        print("z : " + str(z))
        print("x : " + str(x))
        z *= x

    print(z)
    if y < 0:
        z = 1/z

    return z

#------------------------------------------------------------------------------------------------\
#   INVERSE COSINE FUNCTION: ARCCOS(X)
#------------------------------------------------------------------------------------------------

# Using Nvidia's fast approximation
# Absolute error <= 6.7e-5
# reference https://developer.download.nvidia.com/cg/acos.html


def arccos(x):
    if x < 0:
        negate = 1
    else:
        negate = 0

    x = absolute(x)

    # value out of range check
    if x > 1:
        return None

    ret = -0.0187293
    ret = ret * x
    ret = ret + 0.0742610
    ret = ret * x
    ret = ret - 0.2121144
    ret = ret * x
    ret = ret + 1.5707288

    # THIS CONDITIONAL STATEMENT IS BEING USED TO HANDLE INVALID INPUT
    if (exponential((1.0-x), 0.5)  != None):
        ret = ret * exponential((1.0-x), 0.5)
        ret = ret - 2 * negate * ret
        return negate * pi + ret


#------------------------------------------------------------------------------------------------
# SPECIAL EXPONENTIAL FUNCTION: AB^X
#------------------------------------------------------------------------------------------------

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

def log(x,base=10):
    if x<=0:
        return None
    return ln(x)/ln(base)

def ln(x):
    if x<=0 :
        return None

    precision=0.0001
    P=x
    result = 0.0

    while(P >= euler):
        P /= euler
        result+=1

    result += (P / euler)
    P = x

    A = result
    L = (P / taylor_exp(result - 1.0))
    R = ((result - 1.0) * euler)
    result = ((L + R) / euler)

    while absolute(result-A)>precision:
        A = result
        L = (P / taylor_exp(result - 1.0))
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


#------------------------------------------------------------------------------------------------
# STANDARRD DEVIATION FUNCTION: σ(x)
#------------------------------------------------------------------------------------------------

def standard_deviation(*args):
    N = len(args)
    total = 0
    total_squared = 0
    # Step 1, 2
    for i in range(len(args)):
        total += args[i] # sum of dataset
        total_squared += args[i] * args[i]  # sum of the square of the dataset
    # Step 3, 4
    sumOfDistances = (total * total) / N
    # Step 5, 6
    variance = (total_squared - sumOfDistances) / N
    # Step 7
    ans = variance ** 0.5
    return ans


def sinh(x):
    # Calculate the result using the previously defined
    # myPow function
    result = (exponential(euler,x) - exponential(euler,-x))/2
    return result
