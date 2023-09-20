#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 00:45:57 2023

@author: nancyshi
"""
import numpy as np

def quadratic(a, b, c):
    delta = np.sqrt(b*b-4*a*c)
    if b > 0:   
        sol1 = 2*c/(-b-delta)
        sol2 = (-b-delta)/(2*a)
    else:
        sol1 = (-b+delta)/(2*a)
        sol2 = (-b-delta)/(2*a)
    return sol1, sol2



