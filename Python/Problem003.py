N = 600851475143

p = 2
factorization = []

while N > p**2:
    if N % p == 0:
        N /= p
        factorization.append(p)
    else:
        p += 1

print(int(N))
