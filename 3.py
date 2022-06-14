import collections


def lengthOfLongestSubstring(s: str) -> int:
    window = collections.defaultdict(int)

    left = 0
    right = 0

    length = 0

    while right < len(s):
        c = s[right]
        right += 1
        window[c] += 1

        while window[c] > 1:
            pop_c = s[left]
            left += 1
            window[pop_c] -= 1

        length = max(right - left, length)

    return length


s = "pwwkew"
print(lengthOfLongestSubstring(s))
