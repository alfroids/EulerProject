import Functions as func


def is_truncatable_prime(num: int) -> bool:
    my_num = str(num)

    for i in range(1, len(my_num)):
        if not func.is_prime(int(my_num[i:])) or \
           not func.is_prime(int(my_num[:-i])):
            break
    else:
        return True

    return False


sum_ = 0
count = 0
n = 10

while count < 11:
    if func.is_prime(n):
        if is_truncatable_prime(n):
            sum_ += n
            count += 1
    n += 1

print(sum_)