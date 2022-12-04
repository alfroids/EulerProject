import numpy as np

# Using Stirling's approximation:
N = 100
digits = np.zeros(int(np.floor(np.log10(2 * np.pi * N) / 2 + N * np.log10(N / np.e)) + 1))
digits[0] = 1

for k in range(1, N + 1):
    digits *= k
    for j in range(digits.shape[0] - 1):
        digits[j + 1] += digits[j] // 10
        digits[j] %= 10

print(int(np.sum(digits)))
