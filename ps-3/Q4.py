#10.4
from random import random
import numpy as np
import matplotlib.pyplot as plt

tau = 3.053*60
u = np.log(2)/tau

z = np.random.uniform(size=1000)
decay_times = -1/u * (np.log(1-z))
sorted_decay_times = np.sort(decay_times)


notdecayed = np.arange(1000, 0, -1)


plt.plot(sorted_decay_times, notdecayed)
plt.xlabel("Time(s)")
plt.ylabel("Number of Atoms that have not Decayed")
plt.title("Numbers of Atoms that Have not Decayed vs. Time")
plt.show()