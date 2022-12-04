from itertools import permutations


for p in permutations('987654321'):
    pandigital = ''.join(p)
    for i in range(1, 5):
        k = int(pandigital[:i])
        products = [k * n for n in range(1, 10)]
        concatenation = ''
        for j in range(9):
            concatenation += str(products[j])
            if int(concatenation) == int(pandigital):
                print(pandigital)
                exit(0)