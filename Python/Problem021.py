import numpy as np


def get_perfect_divisors(n):
    divs = [1]
    i = 2

    while i <= np.sqrt(n):
        if n % i == 0:
            if n / i == i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(n / i))
        i += 1

    return np.array(divs, dtype=np.int16)


def d(x): return np.sum(get_perfect_divisors(x))


M = 10000
count = 0

for a in range(2, M):
    b = d(a)
    if b != a and d(b) == a:
        count += a

print(count)
