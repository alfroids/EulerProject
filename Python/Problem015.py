N = 20
routes = 1

for i in range(1, N + 1):
	routes *= (i + N) / i

print(round(routes))