def likes(names: list) -> str:
	length = len(names)
	if length == 0:
		return "no one likes this"
	elif length == 1:
		return f"{names[0]} likes this"
	elif length <= 3:
		return ', '.join(names[: -1]) + f' and {names[-1]} like this'
	else:
		return f"{names[0]}, {names[1]} and {length - 2} others like this"

if __name__ == "__main__":
	print(likes(input().split()))