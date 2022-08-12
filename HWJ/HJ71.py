def match(pattern, string):
    m = len(pattern)
    n = len(string)

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = True
        else:
            break

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif pattern[i - 1] == "?" and string[j - 1].isalnum():
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1].lower() == string[j - 1].lower():
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]


while True:
    try:
        pattern = input()
        string = input()

        if match(pattern, string):
            print("true")
        else:
            print("false")
    except:
        break
