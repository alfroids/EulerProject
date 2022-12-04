import Functions as func
import math

sol_max = 0
p_max = 0

for p in range(3, 1001):
    solutions = set()

    for a in range(1, int(p / 3)):
        b = (p * (p - 2 * a)) / (2 * (p - a))
        c = math.sqrt(a**2 + b**2)
        if func.is_integer(b) and func.is_integer(c):
            solutions.add((a, b, c))

    if len(solutions) > sol_max:
        sol_max = len(solutions)
        p_max = p

print(p_max)
