import collections


def checkInclusion(s1: str, s2: str) -> bool:
    need = collections.Counter(s1)
    window = collections.defaultdict(int)

    left = 0
    right = 0
    valid = 0

    while right < len(s2):
        c = s2[right]
        right += 1

        if need[c] > 0:
            window[c] += 1
            if need[c] == window[c]:
                valid += 1

        while (right - left) == len(s1):
            if valid == len(need):
                return True
            pop_c = s2[left]
            left += 1

            if need[pop_c] > 0:
                if window[pop_c] == need[pop_c]:
                    valid -= 1
                window[pop_c] -= 1

    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
