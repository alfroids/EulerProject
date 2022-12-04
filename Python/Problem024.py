import math

pos = 1000000

perm = ""
available = "0123456789"

for i in range(10):
    k = math.ceil(pos / math.factorial(9 - i)) - 1
    perm += available[k]
    available = available[:k] + available[k + 1:]
    pos -= k * math.factorial(9 - i)

print(perm)
