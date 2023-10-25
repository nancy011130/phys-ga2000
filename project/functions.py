import numpy as np
import matplotlib.pyplot as plt
import numba
from numba import njit
from scipy.ndimage import convolve, generate_binary_structure

#initialize lattice, it can be all ups and all downs, or vertain percentage
def initialize_lattice(N, threshold):
    init_random = np.random.random((N, N))
    lattice = np.where(init_random >= threshold, 1, -1)
    return lattice

#Calculate the energy based on the given equaiton using convolution constant mode: sets
#all value om the rim as the defined constant
def Energy(lattice):
    kernal = generate_binary_structure(2, 1)
    kernal[1][1] = False
    total = -lattice * convolve(lattice, kernal, mode='constant', cval=0)
    return total.sum()

#Metropolis, use numba to reduce computation time
@numba.njit("UniTuple(f8[:], 2)(f8, i8[:,:], i8, f8, i8)", nogil=True)
def metropolis(N, spin_arr, times, BJ, E):
    spin_arr_copy = spin_arr.copy()
    net_spins = np.zeros(times-1)
    net_energy = np.zeros(times-1)

    for t in range(0, times-1):
        # Pick random point on array and flip spin
        x, y = np.random.randint(0, N, 2)
        spin_i = spin_arr_copy[x, y]
        spin_f = -spin_i
        
        # Compute energy change after flipping
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        E_i = sum([-spin_i * spin_arr_copy[nx, ny] for nx, ny in neighbors if 0 <= nx < N and 0 <= ny < N])
        E_f = sum([-spin_f * spin_arr_copy[nx, ny] for nx, ny in neighbors if 0 <= nx < N and 0 <= ny < N])

        # Update spin 
        dE = E_f - E_i
        if dE > 0 and np.random.random() < np.exp(-BJ * dE):
            spin_arr_copy[x, y] = spin_f
            E += dE
        elif dE <= 0:
            spin_arr_copy[x, y] = spin_f
            E += dE

        net_spins[t] = spin_arr_copy.sum()
        net_energy[t] = E

    return net_spins, net_energy

@numba.njit("i8[:,:] (f8, i8[:,:], i8, f8, i8)", nogil=True)
def metropolis_plot(N, spin_arr, times, BJ, E):
    spin_arr_copy = spin_arr.copy()
    net_spins = np.zeros(times-1)
    net_energy = np.zeros(times-1)

    for t in range(0, times-1):
        # Pick random point on array and flip spin
        x, y = np.random.randint(0, N, 2)
        spin_i = spin_arr_copy[x, y]
        spin_f = -spin_i
        
        # Compute energy change after flipping
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        E_i = sum([-spin_i * spin_arr_copy[nx, ny] for nx, ny in neighbors if 0 <= nx < N and 0 <= ny < N])
        E_f = sum([-spin_f * spin_arr_copy[nx, ny] for nx, ny in neighbors if 0 <= nx < N and 0 <= ny < N])

        # Update spin 
        dE = E_f - E_i
        if dE > 0 and np.random.random() < np.exp(-BJ * dE):
            spin_arr_copy[x, y] = spin_f
            E += dE
        elif dE <= 0:
            spin_arr_copy[x, y] = spin_f
            E += dE

    return spin_arr_copy


@numba.njit("UniTuple(f8[:], 2)(f8, i8[:,:], i8, f8, i8)", nogil=True)
def metropolis(N, spin_arr, times, BJ, E):
    spin_arr_copy = spin_arr.copy()
    net_spins = np.zeros(times-1)
    net_energy = np.zeros(times-1)

    for t in range(0, times-1):
        # Pick random point on array and flip spin
        x, y = np.random.randint(0, N, 2)
        spin_i = spin_arr_copy[x, y]
        spin_f = -spin_i
        
        # Compute energy change after flipping
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        E_i = sum([-spin_i * spin_arr_copy[nx, ny] for nx, ny in neighbors if 0 <= nx < N and 0 <= ny < N])
        E_f = sum([-spin_f * spin_arr_copy[nx, ny] for nx, ny in neighbors if 0 <= nx < N and 0 <= ny < N])

        # Update spin 
        dE = E_f - E_i
        if dE > 0 and np.random.random() < np.exp(-BJ * dE):
            spin_arr_copy[x, y] = spin_f
            E += dE
        elif dE <= 0:
            spin_arr_copy[x, y] = spin_f
            E += dE

        net_spins[t] = spin_arr_copy.sum()
        net_energy[t] = E

    return net_spins, net_energy


# plot the result
def plot_metropolis_results(N, spins, energies, BJ, E):
    """Plot the evolution of average spin and energy."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    axes[0].plot(spins/N**2)
    axes[0].set_xlabel('Algorithm Time Steps')
    axes[0].set_ylabel(r'Average Spin $\bar{m}$')
    axes[0].grid()
    
    axes[1].plot(energies)
    axes[1].set_xlabel('Algorithm Time Steps')
    axes[1].set_ylabel(r'Energy $E/J$')
    axes[1].grid()
    
    fig.tight_layout()
    fig.suptitle(rf'Evolution of Average Spin and Energy for $\beta J={BJ}$', y=1.07, size=18)
    plt.show()

# get the average spin, energy and energy std
def Spin_energy(N, lattice, BJs):
    """Get average spin, energy mean, and energy std for a range of BJ values."""
    ms = np.zeros(len(BJs))
    E_means = np.zeros(len(BJs))
    E_stds = np.zeros(len(BJs))

    for i, bj in enumerate(BJs):
        spins, energies = metropolis(N, lattice, 1000000, bj, Energy(lattice))
        ms[i] = spins[-100000:].mean() / N**2
        E_means[i] = energies[-100000:].mean()
        E_stds[i] = energies[-100000:].std()

    return ms, E_means, E_stds
