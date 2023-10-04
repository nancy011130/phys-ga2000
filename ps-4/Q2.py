#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:32:06 2023

@author: nancyshi
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw_
#constants:
m = 1


def f(x, b):
  return (b**4-x**4)**(-1/2)

N = 20
a = 0
P_list = []
A_list = np.linspace(0, 2, 100)
for A in A_list:
    b = A
    x, w = gaussxw_(N)
    xp = 0.5*(b-a)*x + 0.5*(b-a)
    wp = 0.5*(b-a)*w
    
    s = 0.0
    for k in range(N):
        s+=wp[k]*f(xp[k], b)
    
    P_list.append(s*np.sqrt(8*m))
plt.plot(A_list, P_list)
plt.xlabel("Amplitude")
plt.ylabel("Period")
plt.title("Period for Different Amplitudes")
