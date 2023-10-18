import numpy as np
from gaussxw import gaussxw_
import math

def gamma_integrand(z, n):
    x = (n-1) * z / (1 - z)
    return np.exp((n-1)*np.log(x) - x) * (n-1) / (1-z)**2

def gamma_function(n, N=50): 
    a = 0
    b = 1
    x, w = gaussxw_(N)
    xp = 0.5 * (b-a) * x + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w

    s = 0
    for k in range(N):
        s += wp[k] * gamma_integrand(xp[k], n)
    return s

print("r(3/2) is", gamma_function(1.5))
print()
print("r(3) = ", gamma_function(3) )
print("Factorial of 3-1: ", math.factorial(2))
print("r(6) = ", gamma_function(6) )
print("Factorial of 6-1: ", math.factorial(5))
print("r(10) = ", gamma_function(10) )
print("Factorial of 10-1: ", math.factorial(9))