import Functions as func
import math


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("ext/p042_words.txt", 'r') as file:
    words = file.readline().strip('\"').split("\",\"")

count = 0

for word in words:
    value = 0
    for letter in word:
        value += alphabet.index(letter) + 1

    n = (math.sqrt(8 * value + 1) - 1) / 2
    if func.is_integer(n):
        count += 1

print(count)