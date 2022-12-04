N = 1001

sum_diag = 1
k = 1

for n in range(3, N + 1, 2):
    for _ in range(4):
        k += n - 1
        sum_diag += k

print(sum_diag)
