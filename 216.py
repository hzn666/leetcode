class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.sum = 0

    def backtrack(self, n, k, start_num):
        if self.sum > n:
            return

        if len(self.path) == k:
            if self.sum == n:
                self.res.append(self.path[:])
            return

        for i in range(start_num, 10 - (k-len(self.path)) + 1):
            self.path.append(i)
            self.sum += i
            self.backtrack(n, k, i + 1)
            self.sum -= i
            self.path.pop()
