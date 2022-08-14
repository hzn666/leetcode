from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtracking(start, path):
            res.append(path)

            if start == len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                backtracking(i + 1, path + [nums[i]])

        backtracking(0, [])
        return res
