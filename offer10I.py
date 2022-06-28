def fib(n: int) -> int:
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % int(1e9 + 7)
    return b