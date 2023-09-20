import time

start = time.time()

def mag(i, j, k):
    return np.sqrt(i**2+j**2+k**2)
import numpy as np
M = 0
L = 100
for i in np.arange(-L, L+1, dtype=float):
  for j in np.arange(-L, L+1, dtype=float):
    for k in np.arange(-L, L+1, dtype=float):
      if ((i != 0) or (j!=0) or (k!=0)):
        M+=((-1)**(i+j+k))/mag(i, j, k)

print("With for loop:", M)
end = time.time()
print(end - start)
