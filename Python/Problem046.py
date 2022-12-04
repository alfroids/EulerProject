import Functions as func
import math


def conjecture(num: int, primes: list) -> bool:
    for p in primes:
        sqr = (num - p) / 2
        if func.is_integer(math.sqrt(sqr)):
            return True

    return False


P = [2]
i = 3

while True:
    if func.is_composite(i):
        if not conjecture(i, P):
            print(i)
            break
    else:
        P.append(i)

    i += 2