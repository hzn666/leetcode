def reverseStr(s: str, k: int) -> str:
    def reverse(s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

    result = list(s)

    for i in range(0, len(s), 2 * k):
        result[i:i + k] = reverse(result[i:i + k])

    return "".join(result)


s = "abcdefg"
k = 2
print(reverseStr(s, k))

