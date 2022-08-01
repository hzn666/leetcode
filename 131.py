class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def partition(self, s):
        if not s:
            return []

        self.backtrack(s, 0)
        return self.res

    def backtrack(self, s, index):
        if len(s) == index:
            self.res.append(self.path[:])
            return

        for i in range(index, len(s)):
            temp = s[index:i + 1]

            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtrack(s, i + 1)
                self.path.pop()
            else:
                continue
