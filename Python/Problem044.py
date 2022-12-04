import Functions as func
import math


def is_pentagonal(num: int) -> bool:
    n = (math.sqrt(24 * num + 1) + 1) / 6
    return func.is_integer(n)


pentagonals = list()
n = 1

while True:
    pent = n * (3 * n - 1) / 2

    for p in pentagonals:
        s = pent + p
        d = pent - p
        if is_pentagonal(s) and is_pentagonal(d):
            print(int(d))
            exit()

    n += 1
    pentagonals.append(pent)