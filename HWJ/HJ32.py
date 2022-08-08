a = input()

dp = [[False] * len(a) for _ in range(len(a))]
res = 1

for i in range(len(a) - 1, -1, -1):
    for j in range(i, len(a)):
        if a[i] == a[j]:
            if j - i <= 1:
                res = max(res, j - i + 1)
                dp[i][j] = True
            elif dp[i + 1][j - 1]:
                res = max(res, j - i + 1)
                dp[i][j] = True

print(res)
