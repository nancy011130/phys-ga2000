#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:55:02 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt

def intergrand(n, x):
    return x**(n-1)*np.exp(-x)

x = np.arange(0, 5, 0.1)
y_2 = []
y_3 = []
y_4 = []
for i in range(len(x)):
    y_2.append(intergrand(2, x[i]))
    y_3.append(intergrand(3, x[i]))
    y_4.append(intergrand(4, x[i]))

print(y_2)
print(x)
plt.plot(x, y_2, label = "n = 2")
plt.plot(x, y_3, label = "n = 3")
plt.plot(x, y_4, label = "n = 4")
plt.legend()
plt.title("Gamma function integrand")
plt.xlabel("x")
plt.ylabel("Intergrand")