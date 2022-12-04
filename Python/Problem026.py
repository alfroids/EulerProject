longest = [0, 0]

for d in range(2, 1000):
    if d % 2 != 0 and d % 5 != 0:
        n = 1
        while 10**n % d != 1:
            n += 1

        if n > longest[1]:
            longest = [d, n]

print(longest[0])
