import math


def get_divisors(num):
	div = []
	i = 1
    
	while i <= math.sqrt(num):
		if (num % i == 0):
			if (num / i == i):
				div.append(i)
			else:
				div.append(i)
				div.append(int(num / i))
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