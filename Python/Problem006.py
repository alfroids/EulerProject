import numpy as np

N = 100
a = np.arange(N) + 1

print(a.sum()**2 - (a**2).sum())