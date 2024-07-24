from itertools import permutations

while True:
	length = int(input('Length of Output: '))
	numbers = input('Numbers: ').split()
	new_numbers = []

	for n in numbers:
		new_numbers.append(int(n))

	numbers = new_numbers
	how_much = 0
	perm = permutations(numbers,length)
	for i in list(perm):
		print(i)
		how_much = how_much + 1
	print('# of permutations:',how_much)
