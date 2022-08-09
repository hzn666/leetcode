class Solution:
    def combine(self, n, k):
        res = []
        path = []

        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(startIndex, n + 1 - (k - len(path) - 1)):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res