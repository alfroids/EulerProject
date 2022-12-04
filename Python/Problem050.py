import math
import numpy as np


primes = list()
primes.append(2)

for i in range(3, 1000000, 2):
    for p in primes:
        if p > math.sqrt(i):
            primes.append(i)
            break
        if i % p == 0:
            break

primes = np.array(primes)

L = 1
while np.sum(primes[:L]) < primes[-1]:
    L += 1

for l in range(L, 0, -1):
    for s in range(primes.shape[0]):
        sum_ = np.sum(primes[s:s + l])
        if sum_ > primes[-1]:
            break
        idx = np.where(primes == sum_)[0]
        if idx.shape[0] > 0:
            print(sum_)
            exit()