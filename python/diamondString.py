def diamond(n: int) -> str:
	if n % 2 == 0 or n < 0:
		return None
	diamondStr = str()
	spaces, star = n // 2, 1
	for _ in range(n // 2):
		diamondStr += ' ' * spaces
		# print(' ' * spaces, end='')
		for _ in range(star):
			# print('*', end='')
			diamondStr += '*'
		diamondStr += '\n'
		star += 2
		spaces -= 1
		# print()
	# print('*' * n)
	diamondStr += '*' * n + '\n'
	star, spaces = n - 2, 1
	for _ in range(n // 2):
		diamondStr += ' ' * spaces
		# print(' ' * spaces, end='')
		for _ in range(star):
			# print('*', end='')
			diamondStr += '*'
		diamondStr += '\n'
		# print()
		star -= 2
		spaces += 1
	return diamondStr

if __name__ == '__main__':
	print(diamond(int(input())))