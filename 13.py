# 罗马数字转整数

class Solution:
    symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        hlevel = 1

        for ch in s[::-1]:
            level = Solution.symbol_values[ch]
            if level >= hlevel:
                ans += level
                hlevel = level
            else:
                ans -= level
        return ans

        # for i, ch in enumerate(s):
        #     value = Solution.symbol_values[ch]
        #     if i < n-1 and value < Solution.symbol_values[s[i+1]]:
        #         ans -= value
        #     else:
        #         ans += value
        #
        # return ans

