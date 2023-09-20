#Question 3
import numpy as np
import matplotlib.pyplot as plt


yes_m = []
no_m = []
trial_yes = []
trial_no = []
N = 10
def Mandelbrot(c):
  z = 0+0j
  for t in range(N):
      if abs(z)>2:
          no_m.append(c)
          trial_no.append(N)
      z = z*z+c
  yes_m.append(c)
  trial_yes.append(t)

x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)
for a in x:
  for b in y:
    c = complex(a, b)
    Mandelbrot(c)
plt.scatter(np.real(yes_m), np.imag(yes_m), c = trial_yes)
plt.scatter(np.real(no_m), np.imag(no_m),c = trial_no )
plt.colorbar()
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

