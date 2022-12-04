import numpy as np


# Parameters:
B = 2
N = 1000
###############

digits = np.zeros(int(1 + N * np.log10(B)))
digits[-1] = 1

for n in range(N):
	digits *= B
	for i in np.argwhere(digits >= 10):
		digits[i - 1] += int(digits[i] / 10)
		digits[i] %= 10

print(int(sum(digits)))
