N, m = list(map(int, input().split()))
N //= 10
k = []
W = {}
V = {}

for i in range(1, m + 1):
    W[i] = [0, 0, 0]
    V[i] = [0, 0, 0]

for i in range(1, m + 1):
    item = list(map(int, input().split()))
    if item[2] == 0:
        W[i][0] = item[0] // 10
        V[i][0] = item[0] // 10 * item[1]
        k.append(i)
    else:
        if W[item[2]][1] == 0:
            W[item[2]][1] = item[0] // 10
            V[item[2]][1] = item[0] // 10 * item[1]
        else:
            W[item[2]][2] = item[0] // 10
            V[item[2]][2] = item[0] // 10 * item[1]

W = [W[i] for i in k]
V = [V[i] for i in k]
length = len(k)

dp = [[0] * (N + 1) for _ in range(length + 1)]
for i in range(1, length + 1):
    w1 = W[i - 1][0]
    w2 = W[i - 1][1]
    w3 = W[i - 1][2]
    v1 = V[i - 1][0]
    v2 = V[i - 1][1]
    v3 = V[i - 1][2]

    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j]
        if j - w1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w1] + v1)
        if j - w1 - w2 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w1 - w2] + v1 + v2)
        if j - w1 - w3 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w1 - w3] + v1 + v3)
        if j - w1 - w2 - w3 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w1 - w2 - w3] + v1 + v2 + v3)

print(dp[length][N] * 10)


