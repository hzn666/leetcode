from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            m = (i + j) // 2

            if nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[j]:
                j = m
        return nums[i]