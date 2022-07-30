from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and not nums[right] % 2:
                right -= 1
            while left < right and nums[left] % 2:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]

        return nums