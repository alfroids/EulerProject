from itertools import permutations


sum_ = 0
primes = [2, 3, 5, 7, 11, 13, 17]

for p in permutations('0123456789'):
    pandigital = ''.join(p)
    for i in range(1, 8):
        if int(pandigital[i:i + 3]) % primes[i - 1] != 0:
            break
    else:
        sum_ += int(pandigital)

print(sum_)