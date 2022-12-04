import numpy as np

powr = 5
count = 0

for i in range(2, 355000):
    digits = np.fromiter(str(i), dtype=np.int32)
    if (digits**powr).sum() == i:
        count += i

print(count)
