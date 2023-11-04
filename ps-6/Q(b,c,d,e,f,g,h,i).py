#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:53:49 2023

@author: nancyshi
"""
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
flux_sum = np.sum(flux, axis = 1)

#Question B
flux_normalized = flux/np.tile(flux_sum, (np.shape(flux)[1], 1)).T
means_normalized = np.mean(flux_normalized, axis=1)
flux_normalized_0_mean = flux_normalized-np.tile(means_normalized, (np.shape(flux)[1], 1)).T

#correlation matrix
r = flux_normalized_0_mean 
r_subset = r[:, :]
logwave_subset = logwave
C = r_subset.T@r_subset

#svd
U, S, Vh = np.linalg.svd(r_subset, full_matrices=True)



def sorted_eigs(r, return_eigvalues = False):
    """
    Calculate the eigenvectors and eigenvalues of the correlation matrix of r
    -----------------------------------------------------
    """
    corr=r.T@r
    eigs=np.linalg.eig(corr) #calculate eigenvectors and values of original 
    arg=np.argsort(eigs[0])[::-1] #get indices for sorted eigenvalues
    eigvec=eigs[1][:,arg] #sort eigenvectors
    eig = eigs[0][arg] # sort eigenvalues
    if return_eigvalues == True:
        return eig, eigvec
    else:
        return eigvec
    


eigvecs_svd = Vh.T
eigvals_svd = S**2
svd_sort = np.argsort(eigvals_svd)[::-1]
eigvecs_svd = eigvecs_svd[:,svd_sort]
eigvals_svd = eigvals_svd[svd_sort]

eigvals, eigvecs = sorted_eigs(r_subset, return_eigvalues = True)

#Question D
for i in range(5):
    plt.plot(logwave, eigvecs[i],label=f'eigvecs {i+1}')
plt.xlabel('Wavelength [$A$]')
plt.ylabel('Eigenvector')
plt.legend()
plt.show() 

#Question E
for i in range(len(eigvecs)):
    plt.plot(eigvecs_svd[:,i], eigvecs[:,i], 'o')
plt.plot(np.linspace(-0.2, 0.2), np.linspace(-0.2, 0.2), label = "Linear Fit")
plt.xlabel('SVD eigenvector')
plt.ylabel('covariance eigenvector')
plt.legend()
plt.show()

#Question G
def PCA(l, r, project = True):
    eigvector = sorted_eigs(r)
    eigvec=eigvector[:,:l] #sort eigenvectors, only keep l
    reduced_wavelength_data= np.dot(eigvec.T,r.T) #np.dot(eigvec.T, np.dot(eigvec,r.T))
    if project == False:
        return reduced_wavelength_data.T # get the reduced wavelength weights
    else: 
        return reduced_wavelength_data.T, np.dot(eigvec, reduced_wavelength_data).T # multiply eigenvectors by 
                                                        # weights to get approximate spectrum
                                                     
plt.plot(logwave,flux_normalized[1],label="data")
plt.plot(logwave,PCA(5,flux_normalized)[1][1],label="approximation")
plt.xlabel('Wavelength [$A$]')
plt.ylabel('Normalized 0-mean flux')
plt.legend()
plt.show()

#Question H, I
def PCA_fast(l, r, eigvec):
    eigvec=eigvec[:,:l] #sort eigenvectors, only keep l
    reduced_wavelength_data= np.dot(eigvec.T,r.T) #np.dot(eigvec.T, np.dot(eigvec,r.T))
    return reduced_wavelength_data.T, np.dot(eigvec, reduced_wavelength_data).T # multiply eigenvectors by 
                                                        # weights to get approximate spectrum
                                                        
def weights(l,r,eigvec):
    eigvec=eigvec[:,l]
    reduced_wavelength_data=np.dot(eigvec.T,r.T)
    return reduced_wavelength_data

c_0=weights(0,flux_normalized, eigvecs_svd)
c_1=weights(1,flux_normalized, eigvecs_svd)
c_2=weights(2,flux_normalized, eigvecs_svd)

plt.scatter(c_0, c_1)
plt.xlabel('c_0')
plt.ylabel('c_1')
plt.show()

plt.scatter(c_0, c_2)
plt.xlabel('c_0')
plt.ylabel('c_2')
plt.ylim(-.001,.001)
plt.show()

N_c=list(range(21))
sq_res=[]
for i in range(21):
    proj=PCA_fast(i+1, flux_normalized, eigvecs_svd)[1]
    res=(flux_normalized-proj)
    sq_res.append(np.sum(res**2))

plt.plot(N_c,sq_res)
plt.xlabel("N_c")
plt.ylabel("Square Residuals")
plt.show()


