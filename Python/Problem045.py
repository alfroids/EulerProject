import Functions as func
import math


def is_triangle(num: int) -> bool:
    n = (math.sqrt(8 * num + 1) - 1) / 2
    return func.is_integer(n)


def is_pentagonal(num: int) -> bool:
    n = (math.sqrt(24 * num + 1) + 1) / 6
    return func.is_integer(n)


n = 144

while True:
    hexa = n * (2 * n - 1)
    
    if is_triangle(hexa) and is_pentagonal(hexa):
        print(hexa)
        exit()

    n += 1