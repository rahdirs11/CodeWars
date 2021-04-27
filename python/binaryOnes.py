def count_bits(n: int) -> int:
    return bin(n)[2: ].count('1')


print(count_bits(int(input())))
