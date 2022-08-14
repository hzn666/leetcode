from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(path):
            if len(path) == len(nums):
                res.append(path)

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                backtracking(path + [nums[i]])

        backtracking([])
        return res
