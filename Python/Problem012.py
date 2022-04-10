import math


def get_divisors(n):
	div = []
	i = 1
    
	while i <= math.sqrt(n):
		if (n % i == 0):
			if (n / i == i):
				div.append(i)
			else:
				div.append(i)
				div.append(int(n / i))
		i += 1

	return div


cont = 0
triangular_number = 0
divisors = []
max_ = 500

while len(divisors) <= max_:
	cont += 1
	triangular_number += cont
	divisors = get_divisors(triangular_number)

print(triangular_number)