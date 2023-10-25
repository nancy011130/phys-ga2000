from random import random, randrange
from math import exp
from numpy import ones, sum
import matplotlib.pyplot as plt

def deltaE(i, j, lattice, J):
    '''Computes the change in energy when a spin at site (i,j) is flipped.'''
    N = len(lattice)
    # Periodic boundary conditions
    top = lattice[(i-1)%N][j]
    bottom = lattice[(i+1)%N][j]
    left = lattice[i][(j-1)%N]
    right = lattice[i][(j+1)%N]
    
    return 2 * J * lattice[i][j] * (top + bottom + left + right)

N = 50                  # Lattice size
steps = 250000          # Number of MC steps
J = 1                   # Exchange energy
k = 1                   # Boltzmann constant (set to 1 for simplicity)
T_values = [0.5 * i for i in range(1, 11)] # Different temperature values for simulation
magnetization = []

for T in T_values:
    lattice = ones([N, N], int)  # Initialize lattice with all spins up for simplicity
    M_values = []

    for _ in range(steps):
        i = randrange(N)
        j = randrange(N)
        
        dE = deltaE(i, j, lattice, J)
        if dE <= 0 or random() < exp(-dE/(k*T)):
            lattice[i][j] *= -1
        
        M = sum(lattice)  # Compute magnetization using equation (3)
        M_values.append(M)
    
    # Average magnetization over the simulation
    avg_M = sum(M_values) / len(M_values)
    magnetization.append(avg_M)

# Plotting
plt.plot(T_values, magnetization, '-o', label="Simulation")
plt.xlabel("Temperature T")
plt.ylabel("Magnetization M")
plt.legend()
plt.show()
