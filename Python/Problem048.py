import Functions as func


sum_ = 0
for i in range(1000):
    sum_ += func.modular_power(i + 1, i + 1, 10**10)

print(sum_ % (10**10))