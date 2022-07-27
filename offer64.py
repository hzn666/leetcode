def sumNums(n):
    return n and (n + sumNums(n - 1))
