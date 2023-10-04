#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 01:36:46 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw_, gaussxwab,H
from scipy.special import roots_hermite
n = 5

def f(x):
    constant = 1/(np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi)))
    return x**2 * (constant*H(n,x))**2

def gquad_hermite(b = 10, N=100): #note that N has to be at least 7, which is explained in the report
    x,w = roots_hermite(N) 
    a = 0
    s = sum(f(x)*w) 
    return s

print(np.sqrt(gquad_hermite()))

