class Solution:
    def combinationSum3(self, k, n):
        res = []

        def backtracking(k, n, startNum, path):
            if sum(path) > n:
                return

            if len(path) == k:
                if sum(path) == n:
                    res.append(path)
                return

            for i in range(startNum, 10 - (k-len(path)-1)):
                backtracking(k, n, i + 1, path + [i])

        backtracking(k, n, 1, [])
        return res