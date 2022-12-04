import Functions as func


n = 1
while True:
    if len(func.get_prime_factors(n)) == 4:
        for i in range(1, 4):
            if len(func.get_prime_factors(n + i)) != 4:
                break
        else:
            print(n)
            break
    n += 1