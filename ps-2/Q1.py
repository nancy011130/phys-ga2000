import numpy as np
from bitstring import BitArray

f_original = 100.98763
f = np.float32(f_original)
int32bits = f.view(np.int32)
bin_representation = '{:032b}'.format(int32bits)
print("Binary representation:", bin_representation)


value = BitArray(bin=bin_representation).int
float_value = np.int32(value).view(np.float32)
print("Float representation:", float_value)

difference = f_original - float_value
print("Difference:", difference)
