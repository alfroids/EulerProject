import math


# GETTERS ########################################
def get_factors(num: int, include_one: bool=True,
                include_num: bool=True, sort: bool=False) -> list[int]:
    factors = list()

    if include_one: factors.append(1)
    if include_num: factors.append(num)

    k = 2
    while k < math.sqrt(num):
        if num % k == 0:
            if num / k == k:
                factors.append(k)
            else:
                factors.append(k)
                factors.append(num // k)
        k += 1

    if sort: return sorted(factors)

    return factors


def get_prime_factors(num: int) -> dict[int, int]:
    factors = dict()

    if num < 2: return factors

    while num % 2 == 0:
        try:
            factors[2] += 1
        except KeyError:
            factors[2] = 1
        num = num // 2
         
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            try:
                factors[i] += 1
            except KeyError:
                factors[i] = 1
            num = num // i
             
    if num > 2:
        try:
            factors[num] += 1
        except KeyError:
            factors[num] = 1

    return factors


# TESTERS ########################################
def is_prime(num: int) -> bool:
    if num <= 3: return num > 1
    if num % 2 == 0 or num % 3 == 0: return False

    limit = int(math.sqrt(num))

    for i in range(5, limit + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


def is_composite(num: int) -> bool:
    return not is_prime(num)


def is_integer(num: float) -> bool:
    return num % 1 == 0


def is_palindromic(num: int) -> bool:
    return num == int(str(num)[::-1])


def is_triangle(num: int) -> bool:
    n = (math.sqrt(8 * num + 1) - 1) / 2
    return is_integer(n)


def is_pentagonal(num: int) -> bool:
    n = (math.sqrt(24 * num + 1) + 1) / 6
    return is_integer(n)


def is_hexagonal(num: int) -> bool:
    n = (math.sqrt(8 * num + 1) + 1) / 4
    return is_integer(n)


# CONVERTERS #####################################
def to_binary(num: int) -> int:
    return int(bin(num)[2:])


# OTHERS #########################################
def replace_char(string: str, at: int, by: str) -> str:
    chars = list(string)
    chars[at] = by
    return ''.join(chars)


def modular_power(base: int, exp: int, mod: int) -> int:
    if mod == 1: return 0

    c = 1
    for _ in range(exp):
        c = (c * base) % mod

    return c
