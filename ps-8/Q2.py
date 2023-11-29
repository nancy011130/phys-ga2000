#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:28:54 2023

@author: nancyshi
"""

from math import sin
from numpy import array, arange
from pylab import plot, xlabel,ylabel, show, legend, title

def f(r, t):
    sigma = 10
    R = 28
    B = 8/3
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = R*x-y-x*z
    fz = x*y-B*z
    return array([fx, fy, fz], float)
a = 0.0
b = 50.0
N = 1000
h = (b-a)/N

tpoints = arange(a, b, h)
xpoints = []
ypoints = []
zpoints = []

r = array([0.0, 1.0, 0.0], float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6
#plot(tpoints, xpoints, label = "x")
plot(tpoints, ypoints, label = "y")
#plot(tpoints, zpoints, label = "z")
xlabel("t")
ylabel("y")
title("Simultaneous ODE")
legend()
show()
plot(xpoints, zpoints)
xlabel("x")
ylabel("z")
title("Strange Attractor")
show()