import math


def get_products(n):
    prods = []
    i = 2

    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i != i:
                s = str(i) + str(int(n / i))
                if len(s) == len(set(s)) and '0' not in s:
                    prods.append(s)
        i += 1

    return prods


count = 0

for num in range(1, 20000):
    num = str(num)
    if len(num) == len(set(num)) and '0' not in num:
        for p in get_products(int(num)):
            if len(num + p) == len(set(num + p)) and len(num + p) == 9:
                count += int(num)
                break

print(count)
