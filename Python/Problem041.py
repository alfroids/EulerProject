from itertools import permutations
import Functions as func


for nums in ['987654321', '87654321', '7654321', '654321', '54321', '4321', '321', '21', '1']:
    for p in permutations(nums):
        pandigital = int(''.join(p))
        if func.is_prime(pandigital):
            print(pandigital)
            exit()