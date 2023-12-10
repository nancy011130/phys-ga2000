#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:50:34 2023

@author: nancyshi
"""

import numpy as np

import matplotlib.pyplot as plt
N = 1000
L = 1e-8
h = 1e-18
h_bar = 1.054571817e-34
m = 9.109*1e-31
a = L/N
a1 = 1+h*(1j*h_bar)/(2*m*a**2)
a2 = -h*(1j*h_bar)/(4*m*a**2)
b1 = 1-h*(1j*h_bar)/(2*m*a**2)
b2 = h*(1j*h_bar)/(4*m*a**2)
x_0= L/2
sig = 1e-10
k = 5e10

B = np.zeros((N-1, N-1), dtype = np.cdouble)
A = np.zeros((N-1, N-1), dtype = np.cdouble)
for i in range(N-1):
    for j in range(N-1):
        if j==i:
            B[i][j] = b1
            A[i][j] = a1
        if j == i+1:
            B[i][j] = b2
            A[i][j] = a2
        if j == i-1:
            B[i][j] = b2
            A[i][j] = a2
            
Ainv=np.linalg.inv(A)
            
psi = np.zeros((N-1), dtype = np.cdouble)
for z in range(N-1):
    psi[z] = np.exp(-(z*a-x_0)**2/(2*sig**2))*np.exp(1j*k*z*a)
timestep = 10000

empty = np.zeros((timestep-1, N-1), dtype = np.cdouble)
empty[0] = psi
for p in range(timestep-2):
    v = np.matmul(B, empty[p])
    #PSI = np.linalg.solve(A, v)
    PSI=Ainv.dot(v)
    empty[p+1] = PSI
times = np.arange(0, timestep, 25)
for t in times:
    #print(np.max(empty[t]))
    plt.plot(empty[t]/np.sum(np.abs(empty[t])**2))
    plt.xlabel("Well Width")
    plt.ylabel("psi")
    plt.title("The Schrodinger equation and the Crank-Nicolson method")
    plt.ylim(-0.04, 0.04)
    plt.show()
