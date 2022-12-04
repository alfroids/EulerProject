import Functions as func
from itertools import permutations


for i in range(1000, 3340):
    if i != 1487 and func.is_prime(i):
        j = i + 3330
        k = i + 6660
        if func.is_prime(j) and func.is_prime(k) and \
            set(str(i)) == set(str(j)) and set(str(i)) == set(str(k)):
            print(str(i) + str(i + 3330) + str(i + 6660))
            break