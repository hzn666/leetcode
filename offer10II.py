def numWays(n: int) -> int:
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1000000007
    return b