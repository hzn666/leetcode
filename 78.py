from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(index, path):
            if len(path) >= 2:
                res.append(path)

            used = []
            for i in range(index, len(nums)):
                if path and path[-1] > nums[i] or nums[i] in used:
                    continue
                used.append(nums[i])
                backtracking(i + 1, path + [nums[i]])

        backtracking(0, [])
        return res
