from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if target <= nums[i]:
                return i

        return n

    def erfen(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l


s = Solution()
print(s.erfen([1, 3, 5, 6], 5))
