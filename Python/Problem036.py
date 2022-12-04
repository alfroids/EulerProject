def is_palindromic(num: int) -> bool:
    return num == int(str(num)[::-1])


def to_binary(num: int) -> int:
    return int(bin(num)[2:])


sum_ = 0

for n in range(1000000):
    b = to_binary(n)
    if is_palindromic(n) and is_palindromic(b):
        sum_ += n

print(sum_)
