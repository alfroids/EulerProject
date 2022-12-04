def get_number_name(N):
	if N > 20 and N % 10 > 0:
		n = N % 10
		N -= n

		return get_number_name(N) + get_number_name(n)

	if N == 1: return "one"
	elif N == 2: return "two"
	elif N == 3: return "three"
	elif N == 4: return "four"
	elif N == 5: return "five"
	elif N == 6: return "six"
	elif N == 7: return "seven"
	elif N == 8: return "eight"
	elif N == 9: return "nine"
	elif N == 10: return "ten"
	elif N == 11: return "eleven"
	elif N == 12: return "twelve"
	elif N == 13: return "thirteen"
	elif N == 14: return "fourteen"
	elif N == 15: return "fifteen"
	elif N == 16: return "sixteen"
	elif N == 17: return "seventeen"
	elif N == 18: return "eighteen"
	elif N == 19: return "nineteen"
	elif N == 20: return "twenty"
	elif N == 30: return "thirty"
	elif N == 40: return "forty"
	elif N == 50: return "fifty"
	elif N == 60: return "sixty"
	elif N == 70: return "seventy"
	elif N == 80: return "eighty"
	elif N == 90: return "ninety"
	else: return ""


def num_to_text(N):
	text = ""

	thousands = int(N / 1000)
	if thousands > 0:
		text += get_number_name(thousands) + "thousand"
	N %= 1000

	hundreds = int(N / 100)
	if hundreds > 0:
		text += get_number_name(hundreds) + "hundred"
	N %= 100

	if len(text) > 0:
		text += "and"

	tens = N
	if tens == 0:
		text = text[:-3]
	else:
		text += get_number_name(tens)

	return text


# Parameters:
max_ = 1000
###############

count_letters = 0

for i in range(1, max_ + 1):
	count_letters += len(num_to_text(i))

print(count_letters)