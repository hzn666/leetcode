import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, l, r):
            if l >= r:
                return
            i = partition(nums, l, r)
            if i == len(nums) - k:
                return
            elif i < len(nums) - k:
                quick_sort(nums, i + 1, r)
            else:
                quick_sort(nums, l, i - 1)

        def partition(nums, l, r):
            ra = random.randrange(l, r + 1)
            nums[l], nums[ra] = nums[ra], nums[l]
            i, j = l, r
            while i < j:
                while i < j and nums[j] >= nums[l]:
                    j -= 1
                while i < j and nums[i] <= nums[l]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            return i

        quick_sort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]
