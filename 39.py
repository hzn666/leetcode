from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(candidates, target, index, path):
            if sum(path) > target:
                return

            if sum(path) == target:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                backtracking(candidates, target, i, path + [candidates[i]])

        backtracking(candidates, target, 0, [])
        return res