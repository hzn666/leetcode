class Solution:
    def missingNumber(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left