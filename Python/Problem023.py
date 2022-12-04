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


def is_abundant(n):
    return np.sum(get_perfect_divisors(n)) > n


abundants = [12]
for k in range(13, 28124):
    if is_abundant(k):
        abundants.append(k)
abundants = np.array(abundants)

numbers = np.arange(28123) + 1

print(np.setdiff1d(numbers, np.triu(abundants + abundants.reshape(-1, 1))).sum())
