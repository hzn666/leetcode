def isPerfect(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)

    if (sum(res) - n) == n:
        return True
    else:
        return False


n = int(input())
res = 0
for i in range(2, n + 1):
    if isPerfect(i):
        res += 1
print(res)
