#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:26:09 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab, H

x = np.linspace(-4,4, 100)
n = [0,1,2,3]

for ni in n:
    constant = 1/(np.sqrt(2**ni*np.math.factorial(ni)*np.sqrt(np.pi)))
    plt.plot(x,constant*np.exp(-x**2/2)*H(ni,x),label=ni)

plt.legend()
plt.xlabel("X")
plt.ylabel("$\psi_n$(x)")
plt.title("Harmonic Oscillator Wavefunctions")
