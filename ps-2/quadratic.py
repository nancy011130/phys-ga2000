#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 00:45:57 2023

@author: nancyshi
"""

def quadratic_3(a, b, c):
    delta = np.sqrt(b*b-4*a*c)
    sol1 = (-b+delta)/(2*a)
    sol2 = 2*c/(-b+delta)
    print(sol1)
    print(sol2)
