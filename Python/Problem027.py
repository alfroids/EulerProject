import math


def is_prime(k):
    if k < 2:
        return False

    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


maximum = [0, 0, 0]

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n * n + a * n + b):
            n += 1

        if n > maximum[-1]:
            maximum = [a, b, n]

print(maximum[0] * maximum[1])
