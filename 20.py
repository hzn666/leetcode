# 有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        if len(str) == 1:
            return False
        left = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                left.append(ch)
            if ch == ')' or ch == ']' or ch == '}':
                if not left:
                    return False
                ch_left = {
                    ')': '(',
                    ']': '[',
                    '}': '{'
                }
                if left.pop() != ch_left[ch]:
                    return False
        if left:
            return False
        return True

    def guanfang(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

mystr = '{[]}'
s = Solution()
print(s.isValid(mystr))
