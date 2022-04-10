nums = [i + 1 for i in range(20)]

i = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
found = False

while not found:
    i += 1
    found = True
    for n in nums:
        if i % n != 0:
            found = False
            break

print(i)
# print(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2 * 2 * 3 * 2)