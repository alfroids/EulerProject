fibonacci = [1, 2]
sum_ = 2
max_ = 4000000

while fibonacci[-1] <= max_:
	f = fibonacci[-1] + fibonacci[-2]
	fibonacci.append(f)
	if f % 2 == 0:
		sum_ += f

print(sum_)