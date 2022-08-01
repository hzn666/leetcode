class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combinationSum(self, candidates, target):
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res

    def backtrack(self, candidates, target, sum_, start_index):
        if sum_ == target:
            self.res.append(self.path[:])
            return

        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target:
                return

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtrack(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()