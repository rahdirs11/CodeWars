def tribonacci(signature: list, n: int):
    if n == 0:  return []
    if n <= 3:  return signature[: n]
    f, s, t = signature
    next = int()
    for i in range(n - 3):
        next = sum((f, s, t))
        f, s, t = s, t, next
        signature.append(next)
    return signature

# print(tribonacci([1, 1, 1], 1))
