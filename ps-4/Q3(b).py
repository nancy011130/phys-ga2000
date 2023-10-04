#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:48:09 2023

@author: nancyshi
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab, H
from scipy.special import roots_hermite


x = np.linspace(-10,10, 100)
ni = 30

constant = 1/(np.sqrt(2**ni*np.math.factorial(ni)*np.sqrt(np.pi)))
plt.plot(x,constant*np.exp(-x**2/2)*H(ni,x),label=ni)

plt.legend()
plt.xlabel("X")
plt.ylabel("$\psi_n$(x)")
plt.title("Harmonic Oscillator Wavefunctions")
