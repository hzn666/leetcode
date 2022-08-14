class Solution:
    def partition(self, s):
        res = []

        if not s:
            return []

        def backtracking(index, path):
            if len(s) == index:
                res.append(path)
                return

            for i in range(index, len(s)):
                temp = s[index:i+1]
                if temp == temp[::-1]:
                    backtracking(i + 1, path + [temp])

        backtracking(0, [])
        return res