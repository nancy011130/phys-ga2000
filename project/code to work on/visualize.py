#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:34:13 2023

@author: nancyshi
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import convolve, generate_binary_structure
from functions import initialize_lattice, Energy, metropolis, metropolis_plot, plot_metropolis_results, Spin_energy
from ipywidgets import interact

N = 200
def display_spin_field(field):
    plt.imshow(field, cmap='gray')
    plt.colorbar()
    plt.show()

initial = initialize_lattice(N, 0.50)
display_spin_field(initial)

spin_arr_copy = metropolis_plot(N, initial, 80000000, 0.5, Energy(initial))
display_spin_field(spin_arr_copy)



