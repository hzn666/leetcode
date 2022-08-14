from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if not s:
            return res

        def isValid(s):
            if len(s) > 1 and s[0] == "0":
                return False
            if not 0 <= int(s) <= 255:
                return False
            return True

        def backtracking(start, segments):
            if len(segments) == 4 and start == len(s):
                res.append(".".join(segments))
                return

            for i in range(start, len(s)):
                addr = s[start:i + 1]
                if isValid(addr):
                    backtracking(i + 1, segments + [addr])
                else:
                    break

        backtracking(0, [])
        return res
