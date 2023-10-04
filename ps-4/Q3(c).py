#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:50:27 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw_, H

x = np.linspace(-4,4, 100)
n = 5

def f(z):
    constant = 1/(np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi)))
    x = z/(1-z**2)
    dx = (1+z**2)/(1-z**2)**2
    return x**2 * (constant*np.exp(-x**2/2)*H(n,x))**2*dx
N = 100
a = -1
b = 1
    
x, w = gaussxw_(N)
xp = 0.5*(b-a)*x + 0.5*(b-a)
wp = 0.5*(b-a)*w
    
s = 0.0
for k in range(N):
    s+=wp[k]*f(xp[k])

print(np.sqrt(s))

