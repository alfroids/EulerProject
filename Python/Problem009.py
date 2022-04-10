min_, max_ = 300, 1000

for c in range(min_, max_):
	for b in range(min_, c):
		a = max_ - (b + c)
		if (a >= b):
			continue
		if (a**2 + b**2 == c**2):
			print(a*b*c)
			exit()