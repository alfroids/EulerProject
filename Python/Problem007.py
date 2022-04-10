import math

def isPrime(n, primes):
	for p in primes:
		if p > math.sqrt(n):
			break
		if n % p == 0:
			return False
	return True


primes = [2]
p = 2
max_ = 10000

while len(primes) <= max_:
	p += 1
	if isPrime(p, primes):
		primes.append(p)

print(p)