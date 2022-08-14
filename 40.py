from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(candidates, target, index, path):
            if sum(path) > target:
                return

            if sum(path) == target:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                backtracking(candidates, target, i + 1, path + [candidates[i]])

        backtracking(candidates, target, 0, [])
        return res