import collections
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    need = collections.Counter(p)
    window = collections.defaultdict(int)

    left = 0
    right = 0
    valid = 0
    res = []

    while right < len(s):
        c = s[right]
        right += 1

        if need[c] > 0:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while right - left >= len(p):
            if valid == len(need):
                res.append(left)
            pop_c = s[left]
            left += 1

            if need[pop_c] > 0:
                if window[pop_c] == need[pop_c]:
                    valid -= 1
                window[pop_c] -= 1

    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))

