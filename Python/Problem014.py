def get_size(n):
	global sequence_size

	if n in sequence_size.keys():
		return sequence_size.get(n)

	if n % 2 == 0:
		size = 1 + get_size(n / 2)
	else:
		size = 1 + get_size(3 * n + 1)

	sequence_size[n] = size
	return size


sequence_size = {1: 1}
longest_sequence = 1
starting_number = 1
min_, max_ = 2, 1000000

for i in range(min_, max_):
	size = get_size(i)
	if size > longest_sequence:
		longest_sequence = size
		starting_number = i

print(starting_number)