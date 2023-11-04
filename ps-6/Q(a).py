#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:06:34 2023

@author: nancyshi
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
for i in range(9713):
    plt.plot(logwave, flux[i, :])
plt.ylim(0, 5000)
plt.ylabel('flux [$10^{−17}$ erg s$^{−1}$ cm$^{−2}$ A$^{-1}$]', fontsize = 16)
plt.xlabel('wavelength [$A$]', fontsize = 16)
plt.title("Flux vs. Wavelength for all Galaxies")