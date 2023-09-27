from random import random
import numpy as np
import matplotlib.pyplot as plt
NBi_1=10000
NTi = 0
NPb = 0
NBi_2 = 0

h = 1.0
p_Pb = 1-2**(-h/(3.3*60))
p_Ti = 1-2**(-h/(2.2*60))
p_Bi1 = 1-2**(-h/(46*60))

tmax = 20000
tpoints =np.arange(0.0,tmax,h)
Bi_1points = []
Tipoints = []
Pbpoints = []
Bi_2points = []

for t in tpoints:
  Bi_1points.append(NBi_1)
  Tipoints.append(NTi)
  Pbpoints.append(NPb)
  Bi_2points.append(NBi_2)
  decay_Pb = 0
  decay_Ti = 0
  decay_Bi_Ti = 0
  decay_Bi_Pb = 0
  for i in range(NPb):
    if random()<p_Pb:
      decay_Pb += 1
  for i in range(NTi):
    if random()<p_Ti:
      decay_Ti += 1
  for i in range(NBi_1):
    if random()<p_Bi1:
        if random()<0.0209:
          decay_Bi_Ti += 1
        else:
          decay_Bi_Pb += 1

  NBi_2+=decay_Pb
  NPb -= decay_Pb

  NPb += decay_Ti
  NTi -= decay_Ti

  NPb += decay_Bi_Pb
  NTi += decay_Bi_Ti
  NBi_1-=decay_Bi_Ti
  NBi_1-=decay_Bi_Pb



plt.plot(tpoints, Bi_1points)
plt.plot(tpoints, Tipoints)
plt.plot(tpoints, Pbpoints)
plt.plot(tpoints, Bi_2points)
plt.title("Number of Different Isotopes vs.Time")
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.legend(["Bi213", "Tl", "Pb", "Bi209"], loc = "upper right")
plt.show()