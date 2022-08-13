class Solution:
    def combine(self, n, k):
        res = []

        def backtracking(n, k, startIndex, path):
            if len(path) == k:
                res.append(path)
                return

            for i in range(startIndex, n+1-(k-len(path)-1)):
                backtracking(n, k, i+1, path + [i])

        backtracking(n, k, 1, [])
        return res