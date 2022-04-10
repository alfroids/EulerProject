def isPalindrome(num):
    reverse = int(str(num)[::-1])
    return reverse == num


d = 3

for i in range((10**d - 1)**2, 0, -1):
    if isPalindrome(i):
        for j in range((10**d - 1), (10**(d - 1) - 1), -1):
            if i % j == 0:
                if (10**(d - 1) - 1) < i / j <= (10**d - 1):
                    print(i)
                    exit()
