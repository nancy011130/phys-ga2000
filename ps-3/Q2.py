#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 02:07:36 2023

@author: nancyshi
"""

import numpy as np
import matplotlib.pyplot as plt
#Using successively larger matrices (10×10, 30×30, etc.) find empirically and plot how the matrix multiplication computation 
#rises with matrix size. Does it rise as N3 as predicted? Use both an explicit function (i.e. the one in the example) and
#use the dot() method. How do they differ?
import time

time_list = []
time_list2 = []
size_list = []
size_list2 = []
N_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for N in N_list:
  count = 0
  start = time.time()
  C = np.zeros([N, N], float)
  A = np.zeros([N, N], float)
  B = np.zeros([N, N], float)
  for i in range(N):
    for j in range(N):
      for k in range(N):
        count+=1
        C[i, j] += A[i, k] * B[k, j]
  end = time.time()
  time_list.append(end - start)
  size_list.append(count)


for N in N_list:
  start = time.time()
  A = np.zeros([N, N], float)
  B = np.zeros([N, N], float)
  np.dot(A, B)
  end = time.time()
  time_list2.append(end - start)
plt.subplot(1,2,1)
plt.plot(N_list, time_list)
plt.plot(N_list, time_list2)
plt.title("Time vs Matrix Size")
plt.xlabel("Matrix Size")
plt.ylabel("Time(s)")

plt.subplot(1,2,2)
plt.plot(size_list, time_list)
plt.plot(size_list, time_list2)
plt.title("Time vs Matrix Size Cubed ")
plt.xlabel("Matrix Size cubed")
plt.ylabel("Time(s)")

plt.subplots_adjust(wspace=1)
plt.tight_layout()

