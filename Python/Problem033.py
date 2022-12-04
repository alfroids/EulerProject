import math


def shared_digit(n, m) -> str | None:
    n = set(str(n))
    m = set(str(m))

    if not n.isdisjoint(m):
        for k in n:
            if k in m:
                return k

    return None


num_prod = 1
den_prod = 1

for den in range(11, 100):
    for num in range(10, den):
        if not den % 10 == 0 and not num % 10 == 0:
            digit = shared_digit(den, num)
            if not (digit is None) and math.gcd(den, num) != 1:
                p = str(num).find(digit)
                num_ = int(str(num)[:p] + str(num)[p + 1:])
                p = str(den).find(digit)
                den_ = int(str(den)[:p] + str(den)[p + 1:])

                if den_ != 0:
                    if num / den == num_ / den_:
                        num_prod *= num_
                        den_prod *= den_

print(int(den_prod / math.gcd(den_prod, num_prod)))
