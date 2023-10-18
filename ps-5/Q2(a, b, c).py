#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 00:01:17 2023

@author: nancyshi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 21:20:50 2023

@author: nancyshi
"""
import numpy as np
import matplotlib.pyplot as plt

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
plt.scatter(time, signal, label = 'signal')
plt.plot(time, ym, 'r-', label = 'fit')


plt.scatter(time, ym-signal, label = 'residual')

plt.legend()
plt.xlabel("time(s)")
plt.ylabel("signal(Hz)")
plt.title("SVD Best Third Order Polynomial fit and Residual")






