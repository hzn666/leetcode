n = int(input())
height = list(map(int, input().split()))


def inc(arr):
    dp = [1 for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp


left = inc(height)
right = inc(height[::-1])[::-1]

sum_ = [left[i] + right[i] - 1 for i in range(len(left))]
print(n - max(sum_))
