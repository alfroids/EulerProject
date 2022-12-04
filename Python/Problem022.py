alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("ext/p022_names.txt", 'r') as file:
    names = file.readline().strip('\"').split("\",\"")

count = 0
names = sorted(names)

for i in range(len(names)):
    score = 0
    for letter in names[i]:
        score += alphabet.index(letter) + 1

    count += score * (i + 1)

print(count)
