#Question 3
import numpy as np
import matplotlib.pyplot as plt


yes_m = []
no_m = []
N = 100
def Mandelbrot(c):
  z = 0+0j
  for trial in range(N):
    if abs(z)>2:
      no_m.append(c)
      return
    z = z*z+c
  yes_m.append(c)
x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)
for a in x:
  for b in y:
    c = complex(a, b)
    Mandelbrot(c)

plt.scatter(np.real(yes_m), np.imag(yes_m), color = 'black', s = 0.1)
plt.scatter(np.real(no_m), np.imag(no_m), color = 'white', s = 0.01, zorder = -1 )
plt.title("Mandelbrot Plot for N =100")
plt.xlabel("X")
plt.ylabel("Y")