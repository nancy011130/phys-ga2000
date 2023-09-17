#Question 4 131-2
import numpy as np

def quadratic_1(a, b, c):
  delta = np.sqrt(b*b-4*a*c)
  sol1 = (-b+delta)/(2*a)
  sol2 = (-b-delta)/(2*a)
  print(sol1)
  print(sol2)

quadratic_1(0.001, 1000, 0.01)

def quadratic_2(a, b, c):
  delta = np.sqrt(b*b-4*a*c)
  sol1 = 2*c/(-b-delta)
  sol2 = 2*c/(-b+delta)
  print(sol1)
  print(sol2)
quadratic_2(0.001, 1000, 0.01)

def quadratic_3(a, b, c):
    delta = np.sqrt(b*b-4*a*c)
    sol1 = (-b+delta)/(2*a)
    sol2 = 2*c/(-b+delta)
    print(sol1)
    print(sol2)
quadratic_3(0.001, 1000, 0.01)
