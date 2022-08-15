from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0] * len(nums)

        if not nums:
            return res

        nums.sort()

        def backtracking(path):
            if len(path) == len(nums):
                res.append(path)
                return

            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = 1
                    backtracking(path + [nums[i]])
                    used[i] = 0

        backtracking([])
        return res
