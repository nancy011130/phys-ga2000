#4.3 Calculating Derivatives
import numpy as np
import matplotlib.pyplot as plt
x = 1
derivative_a = 2*x-1
print("Analytical: ", derivative_a)#analytical solution

def f(x):
  f = x*(x-1)
  return f
def derivative(x, delta):
  return ( f(x + delta) - f(x) ) / delta

print("Definition of derivative: ", derivative(1, 0.01))


list = [10**(-2), 10**(-4), 10**(-6), 10**(-8), 10**(-10), 10**(-12), 10**(-14)]
difference = []
for i, delta in enumerate(list):
  de = derivative(x,delta)
  difference.append(np.absolute(de-derivative_a))
plt.plot(-np.log10(list), np.log10(difference))
plt.title("Accuracy of taking Different Delta Values for Differentiation")
plt.xlabel("Different Delta values in log scale")
plt.ylabel("Absolute error in log value")
#reason: the difference between the two numbers are too small
