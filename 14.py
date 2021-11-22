# 最长公共前缀
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """我的方法"""
        str_first = strs[0]
        str_first_len = len(str_first)
        loc = 1
        flag = False
        while loc <= str_first_len:
            for str in strs[1:]:
                if str_first[:loc] != str[:loc]:
                    flag = True
                    break
            if flag:
                loc -= 1
                break
            loc += 1
        return str_first[:loc]

    def hengxiangsaomiao(self, strs: List[str]) -> str:
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    def zongxiangsousuo(self, strs: List[str]) -> str:
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]

    def fenzhi(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return lcp(0, len(strs) - 1)

    def erfenchazhao(self, strs: List[str]) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
