import math


sum_ = 0

for i in range(3, 2500000):
    if i == sum(math.factorial(int(j)) for j in str(i)):
        sum_ += i

print(sum_)
