
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 21:20:50 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def is_float(string):
    """ True if given string is float else False"""
    try:
        return float(string)
    except ValueError:
        return False

data = []
with open('signal.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        k = i.rstrip().split('|')
        for i in k:
            if is_float(i):
                data.append(float(i)) 

data = np.array(data, dtype='float')
time = data[::2]
signal = data[1::2]

A = np.zeros((len(time), 4))
A[:, 0] = 1.
A[:, 1] = time
A[:, 2] = time**2
A[:, 3] = time**3
(u, w, vt) = np.linalg.svd(A, full_matrices=False)
w_in = np.zeros(np.shape(w))
for i in range(len(w)):
    if w[i] != 0:
        w_in[i] = 1./w[i]   
                           
ainv = vt.transpose().dot(np.diag(w_in)).dot(u.transpose())
        
c = ainv.dot(signal)
ym = A.dot(c) 


N = 10000
#subtract off linear trend
flat_signal = signal-ym

T = time[1]-time[0]
yf = fft(flat_signal)
xf = fftfreq(N, T)[:N//2]
#plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]), '-o')


omega = 2*np.pi*xf[np.argsort(2.0/N * np.abs(yf[0:N//2]))[::-1]][0]
#plt.vlines(omega/(2*np.pi), 0, 10, color = 'red')
# fit full signal
trial = 40
A = np.zeros((len(time), 2*trial+1+1))
A[:, 0] = 1.
A[:, 1] = time
for i in range(1, trial+1):
    A[:, 2*i] = np.cos((i+1)*omega*time)
    A[:, 2*i+1] = np.sin((2*(i+1))*omega*time)
    

(u, w, vt) = np.linalg.svd(A, full_matrices=False)
ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
c = ainv.dot(signal)
ym = A.dot(c) 



plt.plot(time, signal, '.', label='data')
plt.plot(time, ym, '.', label='model')
#plt.scatter(time, ym-signal, label = 'residual', color='orange')
plt.xlabel('t/t_max')
plt.ylabel('y')
plt.legend()
plt.title("Sinusoidal Fit using FFT")



