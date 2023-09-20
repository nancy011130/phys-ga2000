#Question 4 131-2
import numpy as np

def quadratic_1(a, b, c):
  delta = np.sqrt(b*b-4*a*c)
  sol1 = (-b+delta)/(2*a)
  sol2 = (-b-delta)/(2*a)
  return sol1, sol2
quadratic_1(0.001, 1000, 0.01)
print(quadratic_1(0.001, 1000, 0.01))

def quadratic_2(a, b, c):
  delta = np.sqrt(b*b-4*a*c)
  sol1 = 2*c/(-b-delta)
  sol2 = 2*c/(-b+delta)
  return sol1, sol2
quadratic_2(0.001, 1000, 0.01)
print(quadratic_2(0.001, 1000, 0.01))

def quadratic(a, b, c):
    delta = np.sqrt(b*b-4*a*c)
    if b > 0:   
        sol1 = 2*c/(-b-delta)
        sol2 = (-b-delta)/(2*a)
    else:
        sol1 = (-b+delta)/(2*a)
        sol2 = (-b-delta)/(2*a)
    return sol1, sol2

print(quadratic(0.001, 1000, 0.01))
