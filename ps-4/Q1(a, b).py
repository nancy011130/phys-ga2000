#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 21:26:16 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw_
#constants:
V = 1000*1/1e6
rho = 6.022*1e28
theta = 428
k_b = 1.38e-23


def f(x):
  return (x**4*np.exp(x))/((np.exp(x)-1)**2)
N = 50
a = 0
T_list = []
T_temp = np.linspace(5, 500)
for T in T_temp:
    b = theta/T
    
    x, w = gaussxw_(N)
    xp = 0.5*(b-a)*x + 0.5*(b-a)
    wp = 0.5*(b-a)*w
    
    s = 0.0
    for k in range(N):
        s+=wp[k]*f(xp[k])
    
    T_list.append(s*9*V*rho*k_b*(T/theta)**3)
plt.plot(T_temp, T_list)
plt.xlabel("Temperature[K]")
plt.ylabel("Heat Capacity[J/K]")
plt.title("Heat Capacity of a Solid over Different Temperatures")
