class Solution:
    def printNumber(self, n):
        def dfs(x):
            if x == n:
                s = "".join(num[self.start:])
                if s != '0':
                    res.append(int(s))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                num[x] = str(i)
                dfs(x+1)
            self.nine -= 1

        num = ['0'] * n
        res = []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res