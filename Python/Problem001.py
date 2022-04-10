sum_ = 0
max_ = 1000

for i in range(max_):
    if i % 3 == 0 or i % 5 == 0:
        sum_ += i

print(sum_)