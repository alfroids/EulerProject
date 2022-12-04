import math


def get_rotations(num: int) -> set:
    rots = set()
    my_num = str(num)

    for _ in range(len(my_num)):
        my_num = str(my_num)[1:] + str(my_num)[0]
        num = int(my_num)
        rots.add(num)

    return rots


def is_prime(num: int) -> bool:
    if num <= 3:
        return num > 1

    if num % 2 == 0 or num % 3 == 0:
        return False

    limit = int(math.sqrt(num))

    for i in range(5, limit + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


circular_primes = []

for n in range(2, 1000000):
    if n not in circular_primes and is_prime(n):
        rotations = get_rotations(n)
        for i in rotations:
            if not is_prime(i):
                break
        else:
            circular_primes += rotations

print(len(circular_primes))
