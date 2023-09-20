import time
import numpy as np

start = time.time()
L = 100
i = np.arange(-L, L+1, dtype=float)
j = np.arange(-L, L+1, dtype=float)
k = np.arange(-L, L+1, dtype=float)
i_m, j_m, k_m = np.meshgrid(i, j, k)

M = ((-1)**(i_m + j_m + k_m)) / np.sqrt(i_m**2 + j_m**2 + k_m**2)
M[(i_m==0)*(j_m==0)*(k_m==0)] = 0

print("Without for loop", np.sum(M ))
end = time.time()
print(end - start)