#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:57:08 2023

@author: nancyshi
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

piano = np.loadtxt("//Users/nancyshi/Desktop/phys-ga2000/ps-8/piano.txt")
trumpet = np.loadtxt("//Users/nancyshi/Desktop/phys-ga2000/ps-8/trumpet.txt")
N = len(piano)
t = np.linspace(0, 10, 44100)
T = t[1]-t[0]# sample spacing

x = np.arange(1, N+1)
xf = fftfreq(N, T)[:N//2]

pianof = fft(piano)
trumpetf = fft(trumpet)

plt.plot(xf, 2.0/N * np.abs(pianof[0:N//2]))
omega1 = 2*np.pi*xf[np.argsort(2.0/N * np.abs(pianof[0:N//2]))[::-1]][0]
plt.vlines(omega1/(2*np.pi), 0, 2000, color = 'red')

plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('FFT for a Piano Note with Sampling Rate of 44100 samples/s')
plt.show()

plt.plot(xf, 2.0/N * np.abs(trumpetf[0:N//2]))
omega2 = 2*np.pi*xf[np.argsort(2.0/N * np.abs(trumpetf[0:N//2]))[::-1]][0]
plt.vlines(omega2/(2*np.pi), 0, 3000, color = 'red')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('FFT for a Trumpet Note with Sampling Rate of 44100 samples/s')
plt.show()
print("Piano(E4):", omega1)
print("Trumpet(E5):", omega2)