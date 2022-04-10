import math

def isPrime(n, primes):
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			return False
	return True


primes = [2]
min_, max_ = 3, 2000000

for n in range(min_, max_):
	if isPrime(n, primes):
		primes.append(n)

print(sum(primes))