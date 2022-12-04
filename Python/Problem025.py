import math

phi = (1 + math.sqrt(5)) / 2
size = 1000
n = math.ceil((size - 1 + math.log10(5) / 2) / math.log10(phi))     # asymptotic formula

print(n)
