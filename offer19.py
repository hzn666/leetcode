def isMatch(s: str, p: str) -> bool:
    m, n = len(s) + 1, len(p) + 1
    dp = [[False] * n for _ in range(m)]
    dp[0][0] = True

    for j in range(2, n, 2):
        # 当前p为*，则考虑用*匹配前一位的字符，使用两位前的匹配结果
        dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"

    for i in range(1, m):
        for j in range(1, n):
            if p[j - 1] == "*":
                # 如果当前p为*
                if dp[i][j - 2]:
                    # 用*匹配前一位的字符，使用两位前的匹配结果
                    dp[i][j] = True
                elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                    # 如果*前一位的字符能匹配当前s中的字符，则使用s前一位的匹配结果
                    dp[i][j] = True
                elif dp[i - 1][j] and p[j - 2] == ".":
                    # 和上一种情况相同，用.匹配s中的字符
                    dp[i][j] = True
            else:
                # 如果当前p不为*
                if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                    # 判断当前的s和p是否匹配，则使用前一位的匹配结果
                    dp[i][j] = True
                elif dp[i - 1][j - 1] and p[j - 1] == ".":
                    dp[i][j] = True

    return dp[-1][-1]